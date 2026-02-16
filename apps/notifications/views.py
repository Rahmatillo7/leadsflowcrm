from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Faqat ko‘rish uchun: Notification create avtomatik
    """

    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "SUPER_ADMIN":
            return Notification.objects.all()
        # Faqat o‘z kompaniyasi leadlariga tegishli notificationlar
        return Notification.objects.filter(lead__company=user.company).order_by("-created_at")
