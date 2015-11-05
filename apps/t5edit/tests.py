import json
from apps.hello.models import MyData
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm
from .forms import EditForm
from apps.hello.tests import _data


class TestLoginPage(TestCase):
    fixtures = ['user_data.json']

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


class TestEditPage(TestCase):
    fixtures = ['user_data.json']

    def test_edit_page_uses_correct_html(self):
        """/edit/ url must use edit.html"""
        self.client.login(username='admin', password='admin')
        respose = self.client.get(reverse('edit'))

        self.assertTemplateUsed(respose, 'edit.html')

    def test_edit_page_has_any_data(self):
        """test page containt h1 header tag"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit'))

        self.assertIn('edit', response.content)

    def test_edit_page_context_has_edit_form(self):
        """ /edit/ page has edit-form"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit'))

        self.assertIsInstance(response.context['form'], EditForm)

    def test_edit_page_content_has_edit_form(self):
        """ /edit/ page has edit-form"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit'))

        for key in _data.keys():
            self.assertIn('id_' + key, response.content)

        self.assertIn('edit-form', response.content)

    def test_edit_post_ajax_changes_mydata(self):
        """ /edit/ post ajax request must change mydata if its valid"""
        self.client.login(username='admin', password='admin')

        data = _data.copy()
        data['name'] = 'Nigel'

        response = self.client.post(reverse('edit'), data,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(MyData.objects.first().name, data['name'])
        self.assertEquals(json.loads(response.content)['success'], True)

    def test_edit_post_not_ajax_does_not_chane_data(self):
        """ /edit/ post not ajax request must change mydata if its valid"""
        self.client.login(username='admin', password='admin')

        data = _data.copy()
        data['name'] = 'Nigel'

        self.client.post(reverse('edit'), data)

        self.assertNotEquals(MyData.objects.first().name, data['name'])

    def test_not_logged_in_user_cant_get_edit_page(self):
        """not logged in user getting edit page - redirects '/' """
        response = self.client.get(reverse('edit'))

        self.assertRedirects(response, "%s?next=%s" % (
            reverse('login'), reverse('edit')), 302, 200)

    def test_edit_post_with_invalid_data(self):
        """/edit/ post request with invalid data"""
        self.client.login(username='admin', password='admin')

        data = _data.copy()
        data['email'] = 'dasdasdasd'

        response = self.client.post(reverse('edit'), data,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(json.loads(response.content)['success'], False)
        self.assertEquals(json.loads(response.content)['err_msg']['email'][0],
                          'Enter a valid email address.')
