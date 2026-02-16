from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("api/accounts/", include("apps.accounts.urls")),
    path("api/tasks/", include("apps.tasks.urls")),
    path("api/common/", include("apps.common.urls")),
    path("api/notifications/", include("apps.notifications.urls")),
    path("api/companies/", include("apps.companies.urls")),
    path("api/pipelines/", include("apps.pipelines.urls")),
    path("api/billing/", include("apps.billing.urls")),
    path("api/leads/", include("apps.leads.urls")),
]
