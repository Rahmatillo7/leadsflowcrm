from django.contrib.sites import requests
from django.core.mail import send_mail
from django.conf import settings
from .models import Notification

def send_email_notification(lead, subject, message, user=None):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [lead.email],
        fail_silently=False,
    )
    Notification.objects.create(
        lead=lead,
        user=user,
        type="EMAIL",
        message=message,
        sent_at=None  # optional: set after send
    )

def send_telegram_notification(chat_id, message, lead, user=None):
    BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload)
    Notification.objects.create(
        lead=lead,
        user=user,
        type="TELEGRAM",
        message=message
    )