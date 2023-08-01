from django.contrib import admin
from django.urls import path, include
from kiyafetler import views
from django.conf import settings
from django.conf.urls.static import static
from kiyafetler import views as kiyafetler_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', kiyafetler_views.KiyafetList.as_view(), name='ana-sayfa'),
    path('admin/', admin.site.urls),
    path('api/', include('kiyafetler.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api_schema/', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
    path('swagger/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
