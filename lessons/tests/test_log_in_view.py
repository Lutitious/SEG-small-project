from django.test import TestCase
from django import forms
from django.urls import reverse

from lessons.forms import LogInForm
from lessons.models import MusicStudentUser
from lessons.tests.helpers import LoginTester


class LogInTest(TestCase, LoginTester):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.url = '/log_in/'

    def setUp(self):
        self.form = LogInForm()
        self.form_input = {'username': 'test', 'password': 'ThisIsATest1'}
        MusicStudentUser.objects.create_user(username='test',
                                 password='ThisIsATest1',
                                 first_name='Test',
                                 last_name='Test',
                                 email="test@example.com")

    def test_log_in(self):
        response = self.client.get('/log_in/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertIsInstance(form, LogInForm)
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')
        self.assertFalse(form.is_bound)

    def test_form_contains_required_fields(self):
        form = LogInForm()
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
        password_field = form.fields['password']
        self.assertTrue(isinstance(password_field.widget, forms.PasswordInput))

    def test_form_accepts_valid_input(self):
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_rejects_no_username(self):
        self.form_input['username'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_rejects_no_password(self):
        self.form_input['password'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_unsuccessful_log_in(self):
        form_input = {'username': 'test', 'password': 'IncorrectPassword'}
        response = self.client.post(self.url, form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)

    def test_successful_log_in(self):
        form_input = {'username': 'test', 'password': 'ThisIsATest1'}
        response = self.client.post(self.url, form_input, follow=True)
        self.assertTrue(self._is_logged_in())
        response_url = reverse('logged_in')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'logged_in.html')

