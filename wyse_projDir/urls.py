from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from wyse_appDir import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wyse_appDir/', include('wyse_appDir.urls')),  # Include app-specific URLs
    # Add other URL patterns for your project
]

urlpatterns = format_suffix_patterns(urlpatterns)
