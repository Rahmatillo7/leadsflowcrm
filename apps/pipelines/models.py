from django.db import models
from apps.companies.models import Company

# Create your models here.

class Pipeline(models.Model):
    id =models.IntegerField(primary_key=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='pipelines')
    name = models.CharField(max_length=100, null=True, blank=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PipenlineStage(models.Model):
    id =models.IntegerField(primary_key=True, blank=True)
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE, null=True, related_name='pipelines')
    name = models.CharField(max_length=100, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name