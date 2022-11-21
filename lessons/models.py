from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MusicBookingLesson(models.Model):
    booking_date = models.DateField()
    fulfilled_request = models.BooleanField(default=False)

class MusicStudentUser(AbstractUser):
    bio = models.TextField()
