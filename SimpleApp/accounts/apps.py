from django.apps import AppConfig

#### jus account config~
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'User Management'
    
    def ready(self):
        import accounts.models  # Import the signals
