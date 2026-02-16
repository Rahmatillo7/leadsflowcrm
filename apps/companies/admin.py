from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "plan", "lead_limit", "manager_limit", "is_active", "created_at")

