from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm


class TestLoginPage(TestCase):
    def test_login_page_returns_correct_html(self):
        """ login page should use login.html"""
        response = self.client.get('/login/')

        self.assertTemplateUsed(response, 'login.html')

    def test_login_with_valid_data_works(self):
		""" login with valid data redirects to edit page"""
		response = self.client.post('/login/', 
			{'username': 'admin', 'password': 'admin'})

		self.assertRedirects(response, '/edit/')

    def test_login_page_data_has_auth_form(self):
    	""" auth.form must be in page context"""
    	response = self.client.get('/login/')

    	self.assertTrue(
			isinstance(response.context['form'], AuthenticationForm)
			)

	def test_login_page_renders_with_form(self):
		""" page content must page login from"""
        response = self.client.get('/login/')

        self.assertIn('form', response.content)

    def test_home_page_has_login_link(self):
    	"""" home page must contain login link"""
    	response = self.client.get('/')

    	self.assertIn('login_button', response.content)

