from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from user_auth.forms import UserCreationForm
from user_auth.models import User


class UsersAdmin(UserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }

        ),
    )
    fieldsets = (
        ('基本信息', {'fields': ('username', 'password','email')}),
        ('权限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('时间信息', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(Group)
admin.site.register(User,UserAdmin)