from django.test import TestCase
from django.urls import reverse

from lessons.models import MusicStudentUser
from lessons.tests.helpers import LoginTester


class LogOutTest(TestCase, LoginTester):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.url = '/log_out/'

    def setUp(self):
        self.url = reverse('log_out')
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

    def test_log_out_url(self):
        self.assertEqual(self.url, '/log_out/')

    def test_log_out(self):
        self.client.login(username=self.form_input['username'], password=self.form_input['password'])
        self.assertTrue(self._is_logged_in())
        response = self.client.get(self.url, follow=True)
        response_url = reverse('index')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertFalse(self._is_logged_in())
