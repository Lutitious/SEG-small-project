"""Configuration of admin interface for booking lessons and musical student users"""
from django.contrib import admin
from .models import MusicBookingLesson
from .models import MusicStudentUser
# Register your models here.
@admin.register(MusicBookingLesson)
class MusicBookingLessonAdmin(admin.ModelAdmin):
    """Configuration of admin interface for booking lessons"""
    list_display = [
        'booking_date','fulfilled_request',
    ]

@admin.register(MusicStudentUser)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for musical student users."""
    list_display = [
    'username', 'first_name', 'last_name', 'email', 'is_active',
    ]
