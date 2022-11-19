from django.test import TestCase
from django import forms
from lessons.forms import LogInForm
class LogInTest(TestCase):
    def test_log_in(self):
        response = self.client.get('/log_in/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')

    def test_form_contains_required_fields(self):
        form = LogInForm()
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
        password_field = form.fields['password']
        self.assertTrue(isinstance(password_field.widget, forms.PasswordInput))