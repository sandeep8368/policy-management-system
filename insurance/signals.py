from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Policy
from datetime import date, timedelta
from django.core.mail import send_mail


@receiver(post_save, sender = Policy)
def notify_if_expiring(sender, instance, **kwargs):
    if (instance.end_date - date.today()).days <= 15:
        send_mail(
            "Policy Expiry Reminder",
            f"Hi{instance.user.username},your ploicy ends on {instance.end_date}",
            "no-reply@insurance.com",
            [instance.user.email],
            fail_silently=True
        )