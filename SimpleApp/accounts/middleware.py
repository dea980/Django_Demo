from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import redirect_to_login

## 아 로그인 안하면 스케줄로 못들어가게 인바운드 만들었는데 이렇게 해도 되나? 
## Middle ware can control it? i guess? maybe? GPT is god.. please 
class SignupRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URLs that don't require authentication
        exempt_urls = [
            reverse('account_login'),
            reverse('account_signup'),
            reverse('account_reset_password'),
            '/accounts/google/login/',
            '/accounts/google/login/callback/',
        ]

        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect('account_signup')

        response = self.get_response(request)
        return response