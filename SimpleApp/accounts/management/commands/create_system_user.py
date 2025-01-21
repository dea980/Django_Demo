from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
### what is this create_system_user for?

class Command(BaseCommand):
    help = 'Creates a system user for AI responses'

    def handle(self, *args, **kwargs):
        username = 'ai_assistant'
        email = 'ai@system.local'
        password = 'ai_system_user_123'  # Fixed password for system user
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created system user "{username}"'))
        else:
            self.stdout.write(self.style.SUCCESS(f'System user "{username}" already exists'))