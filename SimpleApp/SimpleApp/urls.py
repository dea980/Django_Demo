"""
URL Configuration for SimpleApp project.

This module contains the root URL configurations for the SimpleApp project.
It includes URL patterns for:
- Admin interface
- Scheduler app
- Chat application
- Authentication (using django-allauth)

The default landing page redirects to the scheduler app.
"""

from django.contrib import admin
from django.urls import path, include
import mimetypes
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scheduler/', include('scheduler.urls')),
    path('chat/', include('Message_Chat_app.urls')),
    
    # Custom accounts URLs
    path('accounts/', include('accounts.urls')),
    
    # Authentication URLs (allauth)
    path('accounts/', include('allauth.urls')),
    
    # Make scheduler the default page
    path('', include('scheduler.urls')),
]

if settings.DEBUG:
    mimetypes.add_type("application/javascript", ".js", True)
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns