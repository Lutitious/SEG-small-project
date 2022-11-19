from django.test import TestCase
from django import forms
from lessons.forms import LogInForm
class LogInTest(TestCase):

    def setUp(self):
        self.form = LogInForm()
        self.form_input = {'username': 'test', 'password': 'Password1'}

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
