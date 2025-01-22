from django.urls import path
from . import views
# Define your URL patterns here.
# URL~~ 근데 의문은 pattern 을 좀더 다양하게 할수 있는방법이 있나 ..??
urlpatterns = [
    path('chat/', views.chat_room, name='chat_room'),# chat
    path('chat/<str:room_name>/', views.chat_room, name='chat_room_with_name'), # chat_room_with_name
    path('send-message/', views.send_message, name='send_message'), # send_message
    path('get-messages/', views.get_messages, name='get_messages'), # get_messages
    path('get-messages/<str:room_name>/', views.get_messages, name='get_messages_with_room'), # get_messages_with_room
]