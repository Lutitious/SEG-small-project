"""Configuration of admin interface for lessons"""
from django.contrib import admin
from .models import MusicBookingLesson
# Register your models here.
@admin.register(MusicBookingLesson)
class MusicBookingLessonAdmin(admin.ModelAdmin):
    """Configuration of admin interface for the booking of music lessons"""
    list_display = [
        'booking_date',
    ]
