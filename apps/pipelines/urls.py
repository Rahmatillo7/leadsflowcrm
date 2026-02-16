from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PipelineViewSet, PipelineStageViewSet

router = DefaultRouter()
router.register(r'pipelines', PipelineViewSet, basename='pipeline')
router.register(r'stages', PipelineStageViewSet, basename='pipeline-stage')

urlpatterns = [
    path('', include(router.urls)),
]