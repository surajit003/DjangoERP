from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "gender", "phone_number", "country", "city", "address_one", "address_two"]
    list_filter = ["gender", "country", "city"]
    list_display_links = ["id", "user"]


admin.site.register(UserProfile, UserProfileAdmin)
