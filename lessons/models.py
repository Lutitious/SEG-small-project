from django.db import models

# Create your models here.

class MusicBookingLesson(models.Model):
    booking_date = models.DateField()
