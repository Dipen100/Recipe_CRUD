from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')

admin.site.unregister(User)

admin.site.register(User, CustomUserAdmin)
