from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ['email']
    list_display = ['first_name','last_name','email', 'is_active', 'is_staff', 'is_superuser']


admin.site.register(CustomUser, CustomUserAdmin)