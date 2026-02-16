from django.db import models

# Create your models here.

class Company(models.Model):
     PLAN_CHOICES = (
        ("FREE", "Free"),
        ("BASIC", "Basic"),
        ("PRO", "Pro"),
     )

     id = models.AutoField(primary_key=True, default=1)
     name = models.CharField(max_length=100)
     slug = models.SlugField(max_length=100, unique=True)
     plan = models.CharField(choices=PLAN_CHOICES, max_length=100)
     lead_limit = models.IntegerField(default=0)
     manager_limit = models.IntegerField(default=0)

     is_active = models.BooleanField(default=True)
     trial_ends_at = models.DateTimeField(null=True, blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
         return self.name
