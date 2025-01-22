"""
ASGI config for SimpleApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

## asgi middleware configuration  settings 인데 나중에 Nginx 쓰는건 다른 타입의 미들웨어인가?? 
## 나중에 물어봐야지~ 일단 만들어진거쓰자~
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimpleApp.settings')

application = get_asgi_application()
