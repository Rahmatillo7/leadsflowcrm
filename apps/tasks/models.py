from django.db import models
from apps.accounts.models import User
from apps.leads.models import Leads


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
    )

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("DONE", "Done"),
        ("OVERDUE", "Overdue"),
    )

    id = models.IntegerField(primary_key=True, editable=False)
    lead = models.ForeignKey(Leads, on_delete=models.CASCADE, related_name="tasks")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.title} ({self.lead.name})"