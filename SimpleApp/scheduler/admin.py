from django.contrib import admin
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'status', 'created_at')
    list_filter = ('status', 'date')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
