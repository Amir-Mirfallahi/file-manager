from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('files/', include('file.urls')),
                  path('token', obtain_auth_token, name="obtain_auth_token"),
                  path('auth/', include('authentication.urls')),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
