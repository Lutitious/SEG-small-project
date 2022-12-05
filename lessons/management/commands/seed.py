from django.core.management.base import BaseCommand, CommandError
from ...models import MusicStudentUser, Lesson, Enrolment
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Use faker to create fake data
        fake = Faker()
        # Create 100 fake users
        for i in range(100):
            MusicStudentUser.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                username=fake.user_name(),
                password=fake.password(),
            )
        # Create fake lessons
        for i in range(10):
            Lesson.objects.create(
                name=fake.name(),
                description=fake.text(),
                price=fake.random_int(min=10, max=100),
                duration=fake.random_int(min=30, max=120),
            )
        # Create fake enrolments
        for i in range(1000):
            Enrolment.objects.create(
                student=fake.random_element(MusicStudentUser.objects.all()),
                lesson=fake.random_element(Lesson.objects.all()),
            )
