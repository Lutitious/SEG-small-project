"""Tests of the sign up view."""
from django.contrib.auth.hashers import check_password
from django.test import TestCase
from django.urls import reverse
from lessons.forms import SignUpForm
from lessons.models import MusicStudentUser
from lessons.tests.helpers import LoginTester


class SignUpViewTestCase(TestCase, LoginTester):
    """Tests of the sign up view."""

    def setUp(self):
        self.url = reverse('sign_up')
        self.form_input = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': '@janedoe',
            'email': 'janedoe@example.org',
            'bio': 'I am a Grade 5 in Violin',
            'new_password': 'Password123',
            'password_confirmation': 'Password123'
        }

    def test_sign_up_url(self):
        self.assertEqual(self.url,'/sign_up/')

    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertFalse(form.is_bound)

    def test_unsuccessful_sign_up(self):
        self.form_input['username'] = "bad_username"
        before_count = MusicStudentUser.objects.count()
        response = self.client.post(self.url, self.form_input)
        after_count = MusicStudentUser.objects.count()
        self.assertEqual(before_count, after_count)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertTrue(form.is_bound)
        self.assertFalse(self._is_logged_in())

    def test_successful_sign_up(self):
        before_count = MusicStudentUser.objects.count()
        response = self.client.post(self.url, self.form_input)
        after_count = MusicStudentUser.objects.count()
        self.assertEqual(before_count + 1, after_count)
        response_url = reverse('logged_in')
        self.assertRedirects(response, response_url)
        user = MusicStudentUser.objects.get(username='@janedoe')
        self.assertEqual(user.first_name, 'Jane')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'janedoe@example.org')
        self.assertEqual(user.bio, 'I am a Grade 5 in Violin')
        self.assertTrue(self._is_logged_in())