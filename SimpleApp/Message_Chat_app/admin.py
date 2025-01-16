from django.contrib import admin
from .models import ChatMessage

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
