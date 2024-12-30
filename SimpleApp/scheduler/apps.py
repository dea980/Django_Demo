from django.apps import AppConfig

## please explain this class
# class Application (App): pass # pylint: disable=  operator      
class SchedulerConfig(AppConfig): # pylint: disable= operator
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheduler' # 
