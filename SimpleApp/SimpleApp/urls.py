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
## 메인 어드민이다~ 다른 기능들 합해 놓기~ 

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
    
    # Make scheduler the default page => 이것으로 로그인후 첫페이지로 설저저저저저저정~
    path('', include('scheduler.urls')),
]

if settings.DEBUG: # 호호호호호혹시 모모모모르니 디버그 바 만들어놓고 HTTP랑 다른거 되는지 확인 ~~
    mimetypes.add_type("application/javascript", ".js", True)
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns