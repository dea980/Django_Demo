from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Schedule
from django.utils import timezone
from datetime import datetime

@login_required
def schedule_list(request):
    schedules = Schedule.objects.all().order_by('date', 'time')
    return render(request, 'scheduler/schedule_list.html', {
        'schedules': schedules,
        'current_datetime': timezone.now()
    })

@login_required
def schedule_create(request):
    if request.method == 'POST':
        try:
            date = datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
            time = datetime.strptime(request.POST['time'], '%H:%M').time()
            
            Schedule.objects.create(
                title=request.POST['title'],
                description=request.POST.get('description', ''),
                date=date,
                time=time
            )
            messages.success(request, 'Schedule created successfully!')
            return redirect('schedule_list')
        except Exception as e:
            messages.error(request, f'Error creating schedule: {str(e)}')
    
    return render(request, 'scheduler/schedule_form.html')

@login_required
def schedule_edit(request, pk):
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

@login_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    
    if request.method == 'POST':
        schedule.delete()
        messages.success(request, 'Schedule deleted successfully!')
        return redirect('schedule_list')
    
    return render(request, 'scheduler/schedule_confirm_delete.html', {'schedule': schedule})

@login_required
def schedule_toggle_status(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    
    if schedule.status == 'pending':
        schedule.status = 'completed'
    elif schedule.status == 'completed':
        schedule.status = 'pending'
    
    schedule.save()
    return redirect('schedule_list')
