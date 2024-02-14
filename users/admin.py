from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class UserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "email",
        "first_name",
        "last_name",
    ]


admin.site.register(CustomUser, UserAdmin)