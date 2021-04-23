from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username','email','password','first_name', 'last_name','avatar')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','first_name', 'last_name','avatar','password1', 'password2'),
        }),
    )
    list_display = ('username','email','first_name', 'last_name')
    search_fields = ('username','email','first_name', 'last_name')
    ordering = ('username','email')

