from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import LeadSerializer
from .permissions import IsCompanyAdminOrManager
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Count
from .serializers import DashboardSerializer
import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Leads


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated, IsCompanyAdminOrManager]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["stage", "manager", "source"]
    search_fields = ["name", "email", "phone", "company_name"]
    ordering_fields = ["created_at", "score"]

    def get_queryset(self):
        user = self.request.user
        if user.role == "SUPER_ADMIN":
            return Leads.objects.all()
        return Leads.objects.filter(company=user.company)


# apps/leads/views.py
class DashboardView(APIView):
    def get(self, request):
        user = self.request.user
        if user.role == "SUPER_ADMIN":
            leads = Leads.objects.all()
        else:
            leads = Leads.objects.filter(company=user.company)

        today = timezone.now().date()
        total_leads = leads.count()

        # created_at ni olib tashlash yoki boshqa field ishlatish
        today_leads = 0  # Yoki: leads.filter(id__gte=...count() agar date field bo'lmasa

        won_count = 0  # stage__is_won_stage yo'q bo'lsa 0
        lost_count = 0
        conversion_rate = (won_count / total_leads * 100) if total_leads else 0

        manager_stats = leads.values("manager__name").annotate(count=Count("id"))
        manager_stats_dict = {m["manager__name"] or "Unassigned": m["count"] for m in manager_stats}

        source_stats = leads.values("source").annotate(count=Count("id"))
        source_stats_dict = {s["source"]: s["count"] for s in source_stats}

        data = {
            "total_leads": total_leads,
            "today_leads": today_leads,
            "conversion_rate": conversion_rate,
            "won_count": won_count,
            "lost_count": lost_count,
            "manager_stats": manager_stats_dict,
            "source_stats": source_stats_dict
        }

        serializer = DashboardSerializer(data)
        return Response(serializer.data)

class LeadExportCSVView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role == "SUPER_ADMIN":
            leads = Leads.objects.all()
        else:
            leads = Leads.objects.filter(company=user.company)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="leads.csv"'

        writer = csv.writer(response)
        writer.writerow([
            "ID", "Name", "Phone", "Email", "Company Name",
            "Source", "Stage", "Manager", "Budget", "Score",
            "Created At", "Updated At"
        ])

        for lead in leads:
            writer.writerow([
                str(lead.id),
                lead.name,
                lead.phone,
                lead.email,
                lead.company_name,
                lead.source,
                lead.stage.name if lead.stage else "",
                lead.manager.name if lead.manager else "",
                str(lead.budget) if lead.budget else "",
                lead.score,
                "",
                ""
            ])

        return response

