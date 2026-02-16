from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, DashboardView, LeadExportCSVView

router = DefaultRouter()
router.register(r'', LeadViewSet, basename='lead')

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='lead-dashboard'),
    path('export/', LeadExportCSVView.as_view(), name='lead-export'),
    path('', include(router.urls)),
]