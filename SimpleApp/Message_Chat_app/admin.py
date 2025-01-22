from django.contrib import admin
from .models import ChatMessage

## 여긴 어드민, 세팅~ 모델의 시작~ 허허허허허허  메세지기능을 위한 규격을 만드는곳~ 
## 뭐가 필요하난나자나
## 보여지는거 필더링 필요한거 내용 유저내임 시간정도? 그리고 체팅룸도 잇네~ 
## 허허허 어떻게 만들어야하나나나~

@admin.register(ChatMessage)
# Register the ChatMessage model with the Django admin site.
class ChatMessageAdmin(admin.ModelAdmin):
    """
    ChatMessageAdmin class for the ChatMessage model.
    Defines the fields to be displayed in the admin interface,
    and the filters and search options available for the model.
    """
    list_display = ('user', 'content', 'room', 'timestamp')
    list_filter = ('room', 'timestamp', 'user')
    search_fields = ('content', 'user__username')
    date_hierarchy = 'timestamp'
