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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scheduler/', include('scheduler.urls')),
    path('chat/', include('Message_Chat_app.urls')),
    
    # Authentication URLs
    path('accounts/', include('allauth.urls')),
    
    # Make scheduler the default page
    path('', include('scheduler.urls')),
]