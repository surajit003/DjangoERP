"""_summary_

two signal receivers for the post_save signal. 
The signal receivers are triggered whenever an instance of the model UserProfile is saved.

"""
import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.profiles.models import UserProfile
from DjangoERP.settings import AUTH_USER_MODEL

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    creates a UserProfile instance for the AUTH_USER_MODEL instance 
    (which is expected to be a custom user model) whenever a new user is created. 
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    saves the user_profile instance of the AUTH_USER_MODEL instance whenever it is saved. 
    The user_profile attribute is assumed to be a related UserProfile instance.
    """
    instance.user_profile.save()
    # log a message indicating that a user profile has been created for the user.
    logger.info(f"{instance}'s profile created")
