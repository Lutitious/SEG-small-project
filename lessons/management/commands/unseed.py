from django.core.management.base import BaseCommand, CommandError
from ...models import MusicStudentUser, Lesson, Enrolment


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Delete all the data
        MusicStudentUser.objects.all().delete()
        Lesson.objects.all().delete()
        Enrolment.objects.all().delete()
