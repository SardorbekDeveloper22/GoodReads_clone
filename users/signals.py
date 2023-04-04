from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def send_signup_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome Goodreads clone',
            f'Hi {instance.username}',
            'goodreadsclone22@gmail.com',
            [instance.email],
            fail_silently=True,
        )
