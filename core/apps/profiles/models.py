from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from core.apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")
    
    
class UserProfile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, default="+254710123456"
    )
    about_me = models.TextField(
        verbose_name=_("About me"), default="say something about yourself"
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo/Logo"), default="/profile_default.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("Country"), default="KE", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("City/Town"),
        max_length=180,
        default="Nairobi",
        blank=False,
        null=False,
    )
    address_one = models.CharField(
        verbose_name=_("Address Line One"),
        max_length=250,
        blank=False,
        null=False,
    )
    address_two = models.CharField(
        verbose_name=_("Address Line Two"),
        max_length=250,
        blank=True,
        null=True,
    )
        
    def __str__(self):
        return f"{self.user.username}'s profile"
