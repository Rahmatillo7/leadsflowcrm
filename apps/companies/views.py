from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'

    def get_queryset(self):
        user = self.request.user
        if user.role == 'SUPER_ADMIN':
            return Company.objects.all()
        elif user.company:
            return Company.objects.filter(id=user.company.id)
        return Company.objects.none()

    @action(detail=True, methods=['get'])
    def stats(self, request, slug=None):
        company = self.get_object()
        return Response({
            'name': company.name,
            'plan': company.plan,
            'lead_count': company.users.count(),
            'is_active': company.is_active,
        })