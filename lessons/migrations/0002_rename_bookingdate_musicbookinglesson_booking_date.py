# Generated by Django 4.1.3 on 2022-11-21 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musicbookinglesson',
            old_name='bookingDate',
            new_name='booking_date',
        ),
    ]
