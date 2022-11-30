class LoginTester:
    def _is_logged_in(self):
        return self.client.session.get('_auth_user_id') is not None