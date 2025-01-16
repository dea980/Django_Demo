"""
Chat application views.

This module contains view functions for handling chat-related operations
including displaying chat rooms, sending messages, and retrieving message history.
All views require user authentication.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from .models import ChatMessage
from django.contrib.auth.models import User

@login_required
def chat_room(request):
    """
    Display the chat room with recent messages.

    Renders the chat room template with the 50 most recent messages for the
    specified room. Room name can be provided via query parameter.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered chat room template with messages and room information.
    """
    room_name = request.GET.get('room', 'general')
    messages = ChatMessage.objects.filter(room=room_name).order_by('-timestamp')[:50]
    return render(request, 'chat/chat_room.html', {
        'room_name': room_name,
        'messages': messages,
    })

@login_required
def send_message(request):
    """
    Handle sending new chat messages.

    Processes POST requests to create new chat messages and returns the message
    data as JSON. Only processes messages with content.

    Args:
        request: The HTTP request object containing message content and room name.

    Returns:
        JsonResponse: Contains status and message data if successful, or error message if not.
    """
    if request.method == 'POST':
        content = request.POST.get('content')
        room = request.POST.get('room', 'general')
        
        if content:
            message = ChatMessage.objects.create(
                content=content,
                user=request.user,
                room=room
            )
            
            return JsonResponse({
                'status': 'success',
                'message': {
                    'content': message.content,
                    'username': message.user.username,
                    'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                }
            })
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@login_required
def get_messages(request, room_name='general'):
    """
    Retrieve chat messages for a specific room.

    Fetches messages newer than a specified timestamp if provided.
    Returns up to 50 most recent messages in JSON format.

    Args:
        request: The HTTP request object.
        room_name (str): Name of the chat room (defaults to 'general').

    Returns:
        JsonResponse: Contains status and list of messages with their details.
    """
    last_timestamp = request.GET.get('last_timestamp')
    messages_query = ChatMessage.objects.filter(room=room_name)
    
    if last_timestamp:
        try:
            last_timestamp = timezone.datetime.fromisoformat(last_timestamp)
            messages_query = messages_query.filter(timestamp__gt=last_timestamp)
        except ValueError:
            pass
    
    messages = messages_query.order_by('-timestamp')[:50]
    
    messages_data = [{
        'content': msg.content,
        'username': msg.user.username,
        'timestamp': msg.timestamp.isoformat(),
    } for msg in messages]
    
    return JsonResponse({
        'status': 'success',
        'messages': messages_data
    })
