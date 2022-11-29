"""Configuration of the adminstration interface for microblogs."""
from django.contrib import admin
from .models import MusicStudentUser

@admin.register(MusicStudentUser)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users."""

    list_display = [
    'username', 'first_name', 'last_name', 'email', 'is_active',
    ]
