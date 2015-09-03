from django.test import TestCase


class TestLoginPage(TestCase):
    def test_login_page_returns_correct_html(self):
        """ login page should use login.html"""
        response = self.client.get('/login/')

        self.assertTemplateUsed(response, 'login.html')
