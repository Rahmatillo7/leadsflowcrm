from rest_framework import serializers
from .models import Pipeline, PipenlineStage


class PipelineStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PipenlineStage
        fields = ['id', 'pipeline', 'name', 'order', 'color', 'created_at']
        read_only_fields = ['id', 'created_at']


class PipelineSerializer(serializers.ModelSerializer):
    stages = PipelineStageSerializer(many=True, read_only=True, source='pipelines')

    class Meta:
        model = Pipeline
        fields = ['id', 'company', 'name', 'is_default', 'created_at', 'stages']
        read_only_fields = ['id', 'created_at']