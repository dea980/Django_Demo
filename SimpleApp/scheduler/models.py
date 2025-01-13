"""
Scheduler application models.

This module defines the data models for the scheduler application,
including the Schedule model for managing calendar events and appointments.
"""

from django.db import models
from django.utils import timezone

class Schedule(models.Model):
    """
    Schedule model for managing calendar events and appointments.

    This model stores information about scheduled events including their title,
    description, date/time, and status. It includes functionality to check if
    an event is past due.

    Attributes:
        title (str): The title of the schedule event (max 200 chars)
        description (str): Optional detailed description of the event
        date (Date): The date of the scheduled event
        time (Time): The time of the scheduled event
        created_at (DateTime): Timestamp of when the event was created
        updated_at (DateTime): Timestamp of the last update
        status (str): Current status of the event (pending/completed/cancelled)
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        """
        Returns a string representation of the Schedule object.

        Returns:
            str: A formatted string containing the title, date, and time of the schedule.
        """
        return f"{self.title} - {self.date} {self.time}"

    def is_past_due(self):
        """
        Checks if the scheduled event is past its due date and time.

        This method combines the date and time fields into a datetime object
        and compares it with the current time to determine if the event is past due.

        Returns:
            bool: True if the event is past due, False otherwise.
        """
        schedule_datetime = timezone.make_aware(
            timezone.datetime.combine(self.date, self.time)
        )
        return schedule_datetime < timezone.now()
