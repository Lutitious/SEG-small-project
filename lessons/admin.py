"""Configuration of admin interface for lessons"""
from django.contrib import admin
from .models import MusicStudentUser
# Register your models here.

class MusicStudentUserAdmin(admin.ModelAdmin):
    """Configuration of admin interface for music students"""
    pass
