from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

    fieldsets = (
        [
            "user info", 
            {
                "fields": ['username', 'email', 'password', 'avatar']
            }
        ],
        [
            "Permissions", 
            {
                "fields": ['is_superuser', 'is_staff', 'is_active', 'groups']
            }
        ]
    )

    list_display  = ['username', 'email', 'password', 'avatar']


admin.site.register(CustomUser, CustomUserAdmin)

