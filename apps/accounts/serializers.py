from rest_framework import serializers
from .models import User
from apps.companies.models import Company

class RegistrationSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'company_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

        def create(self, validated_data):
            company_name = validated_data.get('company_name')

            company = Company.objects.create(
                name=company_name,
                slug=company_name.lower().replace(" ", "-")
            )

            user = User.objects.create(
                email=validated_data.get('email'),
                name=validated_data.get('name'),
                role=validated_data.get('role'),
                company=company
            )

            return user