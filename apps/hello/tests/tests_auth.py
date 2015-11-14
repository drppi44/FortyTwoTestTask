from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestLoginPage(TestCase):
    def test_login_page_returns_correct_html_status_code(self):
        """ login page should use login.html"""
        response = self.client.get(reverse('login'))

        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEquals(response.status_code, 200)

    def test_login_with_valid_data_works(self):
        """ login with valid data redirects to login page logged in"""
        self.client.login(username='admin', password='admin')

        self.assertIn('_auth_user_id', self.client.session)

    def test_login_page_data_has_auth_form(self):
        """ auth.form must be in page context"""
        response = self.client.get(reverse('login'))

        self.assertTrue(
            isinstance(response.context['form'], AuthenticationForm)
        )

    def test_login_page_renders_with_form(self):
        """ page content must contain login form"""
        response = self.client.get(reverse('login'))

        self.assertIn('login_form', response.content)
        self.assertIn('id_username', response.content)
        self.assertIn('id_password', response.content)

    def test_home_page_has_login_link(self):
        """" home page must contain login link"""
        response = self.client.get(reverse('login'))

        self.assertIn('login', response.content)
