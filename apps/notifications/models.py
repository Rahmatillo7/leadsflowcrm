from django.db import models
from apps.leads.models import Leads
from apps.accounts.models import User

class Notification(models.Model):
    TYPE_CHOICES = (
        ("EMAIL", "Email"),
        ("TELEGRAM", "Telegram"),
        ("FOLLOW_UP", "Follow-up"),
    )

    id = models.IntegerField(primary_key=True, editable=False)
    lead = models.ForeignKey(Leads, on_delete=models.CASCADE, related_name="notifications")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.lead.name}"
