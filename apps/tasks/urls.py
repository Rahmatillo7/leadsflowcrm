from django.urls import path

from apps.leads.views import LeadExportCSVView

urlpatterns = [
    path('', LeadExportCSVView.as_view(), name='lead-export'),
]
