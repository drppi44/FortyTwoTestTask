from apps.hello.models import MyData
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditForm
from apps.hello.tests import _data


class TestLoginPage(TestCase):
    fixtures = ['my_fixture.json']

    def test_login_page_returns_correct_html_status_code(self):
        """ login page should use login.html"""
        response = self.client.get(reverse('login'))

        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEquals(response.status_code, 200)

    def test_login_with_valid_data_works(self):
        """ login with valid data redirects to login page logged in"""
        response = self.client.post('/login/',
                                    {'username': 'admin', 'password': 'admin'})

        self.assertRedirects(response, reverse('index'))

    def test_login_page_data_has_auth_form(self):
        """ auth.form must be in page context"""
        response = self.client.get('/login/')

        self.assertTrue(
            isinstance(response.context['form'], AuthenticationForm)
        )

    def test_login_page_renders_with_form(self):
        """ page content must contain login form"""

        response = self.client.get('/login/')

        self.assertIn('login_form', response.content)
        self.assertIn('id_username', response.content)
        self.assertIn('id_password', response.content)

    def test_home_page_has_login_link(self):
        """" home page must contain login link"""
        response = self.client.get('/')

        self.assertIn('login', response.content)


class TestEditPage(TestCase):
    fixtures = ['my_fixture.json']

    def test_edit_page_uses_correct_html(self):
        """/edit/ url must use edit.html"""
        self.client.post('/login/', {'username': 'admin', 'password': 'admin'})
        respose = self.client.get('/edit/')

        self.assertTemplateUsed(respose, 'edit.html')

    def test_edit_page_has_any_data(self):
        """test page containt h1 header tag"""
        self.client.post('/login/', {'username': 'admin', 'password': 'admin'})
        response = self.client.get('/edit/')

        self.assertIn('edit', response.content)

    def test_edit_page_context_has_edit_form(self):
        """ /edit/ page has edit-form"""
        self.client.post('/login/', {'username': 'admin', 'password': 'admin'})
        response = self.client.get('/edit/')

        self.assertIsInstance(response.context['form'], EditForm)

    def test_edit_page_content_has_edit_form(self):
        """ /edit/ page has edit-form"""
        self.client.post('/login/', {'username': 'admin', 'password': 'admin'})
        response = self.client.get('/edit/')

        for key in _data.keys():
            self.assertIn('id_'+key, response.content)

        self.assertIn('edit-form', response.content)

    def test_edit_post_changes_mydata(self):
        """ /edit/ post request must change mydata if its valid"""
        self.client.post('/login/', {'username': 'admin', 'password': 'admin'})

        data = _data.copy()
        data['name'] = 'Nigel'
        self.client.post('/edit/', data)

        self.assertEquals('Nigel', MyData.objects.first().name, data['name'])
