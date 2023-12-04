from .models import Profile
import logging
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


loger = logging.getLogger('recipe_logger')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Profile creation signal"""
    if created:
        profile = Profile.objects.create(
            user=instance,
            email=instance.email,
            nickname=instance.username
        )
        Profile.save(profile)
        loger.info(f'profile for user {instance.username} has been created')
