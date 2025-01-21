from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.http import JsonResponse

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
