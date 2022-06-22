from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = CustomUser
    ordering = ('-date_added',)
    list_display = ('email', 'user_name', 'moderator', 'site_user', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'user_name',)}),
        ('Permissions', {'fields': ('moderator', 'site_user', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'moderator', 'is_staff', 'is_active', 'site_user', 'password1', 'password2')}
         ),
    )


# My registered models.

admin.site.register(CustomUser, UserAdminConfig)
