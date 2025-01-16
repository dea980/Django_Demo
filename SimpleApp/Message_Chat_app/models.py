"""
체팅을 위한 모델

이곳에선 체팅을 위한 데이터 모델을 구성함. 예를 들어 체팅 저장하는것들
데이터 저장하는 방식 UML 디자인한거 ... 
"""

from django.db import models
from django.contrib.auth.models import User
from scheduler.models import Schedule

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
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True, blank=True)
    room = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        # If this message is associated with a schedule, use its chat room
        if self.schedule and not self.room:
            self.room = self.schedule.chat_room
        # If no room is specified and no schedule, use 'general'
        elif not self.room:
            self.room = 'general'
        super().save(*args, **kwargs)
    
    ## 메타 데이터 클래스
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
