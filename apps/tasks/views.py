from rest_framework import viewsets, permissions
from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'SUPER_ADMIN':
            return Task.objects.all()

        return Task.objects.filter(lead__company=user.company)