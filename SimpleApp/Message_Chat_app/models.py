"""
Chat application models.

This module defines the data models for the chat application,
including the ChatMessage model for storing messages in chat rooms.
"""

from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    """
    ChatMessage model for storing chat messages.

    This model represents individual chat messages in the system, storing the message
    content, timestamp, sender information, and the chat room it belongs to.

    Attributes:
        content (str): The actual message text
        timestamp (DateTime): When the message was sent (auto-set)
        user (User): Reference to the user who sent the message
        room (str): The chat room identifier where the message was sent
    """
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.CharField(max_length=100, default='general')
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        """
        Returns a string representation of the ChatMessage object.

        Returns:
            str: A formatted string containing the username and first 50 characters
                 of the message content.
        """
        return f"{self.user.username}: {self.content[:50]}"
