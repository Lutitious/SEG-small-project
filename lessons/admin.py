"""Configuration of the adminstration interface for microblogs."""
from django.contrib import admin
from .models import MusicStudentUser, Lesson, Enrolment, Request


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


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for lessons."""

    list_display = ['title', 'description', 'date', 'time', 'duration', 'price', 'teacher']
    list_filter = ['title', 'description', 'date', 'time', 'duration', 'price', 'teacher']
    search_fields = ['title', 'description', 'date', 'time', 'duration', 'price', 'teacher']
    ordering = ['title']
    fieldsets = ((None, {'fields': ('title', 'description', 'date', 'time', 'duration', 'price', 'teacher')}),)
    add_fieldsets = (
        (None,
         {'classes': ('wide',), 'fields': ('title', 'description', 'date', 'time', 'duration', 'price', 'teacher')}),)
    filter_horizontal = ()


@admin.register(Enrolment)
class EnrolmentAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for enrolment."""

    list_display = ['lesson', 'student']
    list_filter = ['lesson', 'student']
    search_fields = ['lesson', 'student']
    ordering = ['lesson']
    fieldsets = ((None, {'fields': ('lesson', 'student')}),)
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('lesson', 'student')}),)
    filter_horizontal = ()


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """Configuration of the admin interface for requests."""

    list_display = ['lesson', 'student']
    list_filter = ['lesson', 'student']
    search_fields = ['lesson', 'student']
    ordering = ['lesson']
    fieldsets = ((None, {'fields': ('lesson', 'student')}),)
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('lesson', 'student')}),)
    filter_horizontal = ()
