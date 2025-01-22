from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

## 여기에 사인업후 만들어진 프로필 만듬 ~ CASCADE로 유저 삭제시 프로필 DB 에서 삭제하는게 나을라나..
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.URLField(max_length=1024, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

"""
    A decorator for connecting receivers to signals. Used by passing in the
    signal (or list of signals) and keyword arguments to connect::

        @receiver(post_save, sender=MyModel)
        def signal_receiver(sender, **kwargs):
            ...

        @receiver([post_save, post_delete], sender=MyModel)
        def signals_receiver(sender, **kwargs):
            ...
"""
## 이 리시버 되겠지...? 되라 ~ 될꺼다~ 난 잘 읽엇다~ 안돼지마라~ 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a UserProfile instance when a new User is created"""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the UserProfile instance when the User is saved"""
    if hasattr(instance, 'profile'):
        instance.profile.save()
