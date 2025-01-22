from django.apps import AppConfig


# just make this to handle db style for schdule 
class SchedulerConfig(AppConfig): 
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheduler' # 
