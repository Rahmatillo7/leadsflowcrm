from django.db import models
from apps.accounts.models import User
from apps.companies.models import Company
from apps.pipelines.models import PipenlineStage

from django.core.exceptions import ValidationError


# Create your models here.

class Leads(models.Model):

    SOURCE_CHOICES = (
    ('WEBSITE', 'Website'),
    ("TELEGRAM", "Telegram"),
    ('FOOCBOOK', 'foocbook'),
    ("API", 'api')
    )

    id = models.IntegerField(primary_key=True, default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='leads')
    manager = models.ForeignKey(User, on_delete=models.CASCADE,related_name='manager')
    stage = models.ForeignKey(PipenlineStage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company_name = models.CharField(max_length=100)

    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    score = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    tags = models.JSONField(default=list, blank=True)
    custom_fields = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.name} ({self.company_name})"

    def calculate_score(self):
        score = 0
        if self.phone:
            score += 10
        if self.email:
            score += 10
        if self.company_name:
            score += 15
        if self.budget and self.budget > 1000:
            score += 20
        self.score = score



        def validate_lead_limit(user):
            company = user.company
            lead_count = company.leads.count()
            if company.plan == "FREE" and lead_count >= 100:
                raise ValidationError("Lead limit reached for Free plan.")
            elif company.plan == "BASIC" and lead_count >= 5000:
                raise ValidationError("Lead limit reached for Basic plan.")


