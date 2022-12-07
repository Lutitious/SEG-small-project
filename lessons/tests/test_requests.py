from django.test import TestCase
from django import forms
from django.urls import reverse
from django.contrib import messages

from lessons.forms import LogInForm, RequestBookingForm
from lessons.models import MusicStudentUser, Request
from lessons.tests.helpers import LoginTester


def setUp(self):
    self.url = reverse('log_in')
    self.form_input = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'username': '@janedoe',
        'email': 'janedoe@example.org',
        'bio': 'I am a Grade 5 in Violin',
        'password': 'Password123',
        'is_active': True,
    }
    self.User = MusicStudentUser.objects.create_user(**self.form_input)
#     Create a superuser
    self.Admin_User = MusicStudentUser.objects.create_superuser(
        username = '@admin',
        password = 'Password123',
        email = 'admin@example.com',
        first_name = 'Admin',
        last_name = 'User',
        bio = 'I am an admin',
    )


def test_create_request(self):
    response = self.client.get('/request/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'request.html')
    form = response.context['form']
    self.assertIsInstance(form, RequestBookingForm)
    self.assertContains(response, 'Lesson')
    self.assertFalse(form.is_bound)

def test_request_shows_in_admin(self):
    self.client.login(username = '@admin', password = 'Password123')
    response = self.client.get('/admin/lessons/request/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'admin/change_list.html')
    self.assertContains(response, 'Requests')
