from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('commercials.urls')),
    path('blogs/', include('blog.urls')),
    # path('', include('Locals.urls')),
    path('account/', include('api.urls')),
    path('calculators/', include('calculators.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


admin.site.site_header = "LABELLORE"
admin.site.site_title = "LABELLORE"
admin.site.index = "Welcome to Admin Dashboard"

