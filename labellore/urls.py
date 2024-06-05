from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('commercials.urls')),
    path('blogs/', include('blog.urls')),
    path('', include('Locals.urls')),
    path('api/', include('api.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


admin.site.site_header = "LABELLORE"
admin.site.site_title = "LABELLORE"
admin.site.index = "Welcome to Admin Dashboard"