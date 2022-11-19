from django.test import TestCase

class LogInTest(TestCase):
    def test_log_in(self):
        response = self.client.get('/log_in/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')