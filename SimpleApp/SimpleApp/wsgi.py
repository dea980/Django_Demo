"""
WSGI config for SimpleApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
## 읽어보니 서버족 Middleware 인듯? Apache 로도 바꿀수 있나? 나중에 DB 관리할때 생각좀 대봐야겠넹~
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimpleApp.settings')

application = get_wsgi_application()
