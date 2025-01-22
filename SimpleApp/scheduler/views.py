"""
Scheduler application views.

This module contains view functions for handling schedule-related operations
including listing, creating, editing, and deleting schedules. All views require
user authentication.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Schedule
from django.utils import timezone
from datetime import datetime
## TODO: support multiple schedules for different 
@login_required
def schedule_list(request):
    """
    Display a list of all schedules ordered by date and time.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered template with all schedules and current datetime.
    """
    schedules = Schedule.objects.all().order_by('date', 'time')
    return render(request, 'scheduler/schedule_list.html', {
        'schedules': schedules,
        'current_datetime': timezone.now()
    })
## create a new schedule
@login_required
def schedule_create(request):
    """
    Create a new schedule entry.

    Handles both GET requests (display form) and POST requests (create schedule).
    Validates and processes form data, creating a new Schedule object.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered form template or redirect to schedule list on success.
    """
    if request.method == 'POST':
        try:
            date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
            time = datetime.strptime(request.POST['time'], '%H:%M').time()
            
            schedule = Schedule.objects.create(
                title=request.POST['title'],
                description=request.POST.get('description', ''),
                date=date,
                time=time
            )
            # The chat_room field will be automatically generated in the save method
            messages.success(request, 'Schedule created successfully!')
            return redirect('schedule_list')
        except Exception as e:
            messages.error(request, f'Error creating schedule: {str(e)}')
    
    return render(request, 'scheduler/schedule_form.html')
## edting the schedule
@login_required
def schedule_edit(request, pk):
    """
    Edit an existing schedule entry.

    Handles both GET requests (display form with current data) and POST requests
    (update schedule). Validates and processes form data for updating.

    Args:
        request: The HTTP request object.
        pk (int): Primary key of the schedule to edit.

    Returns:
        HttpResponse: Rendered form template or redirect to schedule list on success.
    """
    schedule = get_object_or_404(Schedule, pk=pk)
    
    if request.method == 'POST':
        try:
            schedule.title = request.POST['title']
            schedule.description = request.POST.get('description', '')
            schedule.date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
            schedule.time = datetime.strptime(request.POST['time'], '%H:%M').time()
            schedule.status = request.POST.get('status', 'pending')
            schedule.save()
            
            messages.success(request, 'Schedule updated successfully!')
            return redirect('schedule_list')
        except Exception as e:
            messages.error(request, f'Error updating schedule: {str(e)}')
    
    return render(request, 'scheduler/schedule_form.html', {'schedule': schedule})
# delete the schedule
@login_required
## pk = primary key
def schedule_delete(request, pk):
    """
    Delete an existing schedule entry.

    Handles both GET requests (confirmation page) and POST requests (actual deletion).

    Args:
        request: The HTTP request object.
        pk (int): Primary key of the schedule to delete.

    Returns:
        HttpResponse: Rendered confirmation template or redirect to schedule list on success.
    """
    schedule = get_object_or_404(Schedule, pk=pk)
    
    if request.method == 'POST':
        schedule.delete()
        messages.success(request, 'Schedule deleted successfully!')
        return redirect('schedule_list')
    
    return render(request, 'scheduler/schedule_confirm_delete.html', {'schedule': schedule})

## complete or pending
@login_required
def schedule_toggle_status(request, pk):
    """
    Toggle the status of a schedule between 'pending' and 'completed'.

    Provides a quick way to mark schedules as completed or revert them back to pending.

    Args:
        request: The HTTP request object.
        pk (int): Primary key of the schedule to toggle.

    Returns:
        HttpResponse: Redirect to schedule list after toggling status.
    """
    schedule = get_object_or_404(Schedule, pk=pk)
    
    if schedule.status == 'pending':
        schedule.status = 'completed'
    elif schedule.status == 'completed':
        schedule.status = 'pending'
    
    schedule.save()
    return redirect('schedule_list')
