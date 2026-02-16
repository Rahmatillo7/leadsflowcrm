from rest_framework import serializers

from apps.leads.models import Leads


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = "__all__"
        read_only_fields = ("score", "company", "created_at", "updated_at")

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["company"] = user.company
        lead = Leads.objects.create(**validated_data)
        lead.calculate_score()
        lead.save()
        return lead

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.calculate_score()
        instance.save()
        return instance


from rest_framework import serializers

class DashboardSerializer(serializers.Serializer):
    total_leads = serializers.IntegerField()
    today_leads = serializers.IntegerField()
    conversion_rate = serializers.FloatField()
    won_count = serializers.IntegerField()
    lost_count = serializers.IntegerField()
    manager_stats = serializers.DictField()
    source_stats = serializers.DictField()
