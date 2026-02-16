from rest_framework import viewsets, permissions
from .models import Pipeline, PipenlineStage
from .serializers import PipelineSerializer, PipelineStageSerializer


class PipelineViewSet(viewsets.ModelViewSet):
    serializer_class = PipelineSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'SUPER_ADMIN':
            return Pipeline.objects.all()
        return Pipeline.objects.filter(company=user.company)

    def perform_create(self, serializer):
        if self.request.user.role != 'SUPER_ADMIN':
            serializer.save(company=self.request.user.company)
        else:
            serializer.save()


class PipelineStageViewSet(viewsets.ModelViewSet):
    serializer_class = PipelineStageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'SUPER_ADMIN':
            return PipenlineStage.objects.all()
        return PipenlineStage.objects.filter(pipeline__company=user.company)