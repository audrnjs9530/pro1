from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Artist Info', {
            'fields': ('is_artist', 'nickname'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Artist Info', {
            'fields': ('is_artist', 'nickname'),
        }),
    )

admin.site.register(User, CustomUserAdmin)