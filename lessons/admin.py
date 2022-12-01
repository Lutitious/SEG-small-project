"""Configuration of the adminstration interface for microblogs."""
from django.contrib import admin
from .models import MusicStudentUser


@admin.register(MusicStudentUser)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for users."""

    list_display = [
        'username', 'first_name', 'last_name', 'email', 'is_active',
    ]
    list_filter = ['is_active']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    ordering = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio')}))
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username ', 'password', 'first_name', 'last_name', 'email', 'bio')}),)
    filter_horizontal = ()




