from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.http import JsonResponse
## User profile settings~ 아 몰라 그냥 해~ 사진 , bio, 이름~, discription 정도면 되겠지~ 
## 이름은 에딧팅 되도록 하고 사진도 그렇게~ 그냥 링크인 기능 참고 하나~  그럼 흠.. 
## 프로필 만들어~  사진 은 없지만 디폴트 만들어나야 나중에 업뎃할때 편알듯?
@login_required
def profile(request):
    """
    Display and update user profile.
    """
    user_profile = request.user.profile
    
    if request.method == 'POST':
        # Handle photo update
        photo_url = request.POST.get('photo_url')
        if photo_url:
            user_profile.avatar = photo_url
            user_profile.save()
            messages.success(request, 'Profile photo updated successfully!')
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'No photo URL provided'})
    
    return render(request, 'accounts/profile.html', {
        'profile': user_profile
    })

# 프로필 업뎃해~  아 뭐 여기에 걍 에딧팅 가능하게 오픈 시켜놓고 세이브? 
@login_required
def update_profile(request):
    """
    Update user profile information.
    """
    if request.method == 'POST':
        user = request.user
        user_profile = user.profile
        bio = request.POST.get('bio')
        birth_date = request.POST.get('birth_date')
        username = request.POST.get('username')
        
        if bio:
            user_profile.bio = bio
        if birth_date:
            user_profile.birth_date = birth_date
        if username and username != user.username:
            if not User.objects.filter(username=username).exists():
                user.username = username
                user.save()
            else:
                messages.error(request, 'Username already taken!')
                return redirect('profile')
            
        user_profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
        
    return redirect('profile')
