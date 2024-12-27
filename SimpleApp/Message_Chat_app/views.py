from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from .models import ChatMessage
from django.contrib.auth.models import User

@login_required
def chat_room(request, room_name='general'):
    messages = ChatMessage.objects.filter(room=room_name).order_by('-timestamp')[:50]
    return render(request, 'chat/chat_room.html', {
        'room_name': room_name,
        'messages': messages,
    })

@login_required
def send_message(request):
    if request.method == 'POST': ## POST request
        content = request.POST.get('content')
        room = request.POST.get('room', 'general')
        
        if content: # Post Message
            message = ChatMessage.objects.create(
                content=content,
                user=request.user,
                room=room
            )
            
            return JsonResponse({
                'status': 'success',## status 
                'message': {
                    'content': message.content, ## message content
                    'username': message.user.username, ## 
                    'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                }
            })
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required ## Login require
## get message 
def get_messages(request, room_name='general'): 
    
    last_timestamp = request.GET.get('last_timestamp')
    messages_query = ChatMessage.objects.filter(room=room_name)
    
    if last_timestamp: # last_timestamp ... 
        try:
            last_timestamp = timezone.datetime.fromisoformat(last_timestamp) 
            messages_query = messages_query.filter(timestamp__gt=last_timestamp)
        except ValueError:
            pass
    ## message query
    messages = messages_query.order_by('-timestamp')[:50] ## message
    
    ################################################################
    messages_data = [{
        'content': msg.content, ## message content
        'username': msg.user.username, ## user username
        'timestamp': msg.timestamp.isoformat(), ## timestamp
    } for msg in messages]
    
    return JsonResponse({
        'status': 'success', ## status
        'messages': messages_data ## messages
    })
