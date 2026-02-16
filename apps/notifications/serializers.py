from rest_framework import serializers
from .models import Notification
from apps.leads.serializers import LeadSerializer
from apps.accounts.serializers import RegistrationSerializer

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['id', 'created_at']