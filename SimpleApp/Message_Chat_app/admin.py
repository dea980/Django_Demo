from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'room', 'timestamp')
    list_filter = ('room', 'timestamp', 'user')
    search_fields = ('content', 'user__username')
    date_hierarchy = 'timestamp'
