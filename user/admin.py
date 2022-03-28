from django.contrib import admin
from .models import UserDetails


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'state', 'mobile_no']
