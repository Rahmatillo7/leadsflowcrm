from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.leads.models import Leads
from apps.notifications.services import send_email_notification

@receiver(post_save, sender=Leads)
def send_lead_notification(sender, instance, created, **kwargs):
    if created:
        send_email_notification(instance, "New Lead Created", f"Lead {instance.name} was created")
