import json
from apps.hello.models import UserProfile
from django.core.urlresolvers import reverse
from django.test import TestCase
from apps.hello.forms import EditForm
from apps.hello.tests.tests_home_page import user_data


class TestEditPage(TestCase):
    def test_edit_page_uses_correct_html(self):
        """/edit/ url must use edit.html"""
        self.client.login(username='admin', password='admin')
        respose = self.client.get(reverse('edit'))

        self.assertTemplateUsed(respose, 'hello/edit.html')

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

        for key in user_data.keys():
            self.assertIn('id_' + key, response.content)

        self.assertIn('edit-form', response.content)

    def test_edit_post_ajax_changes_UserProfile(self):
        """ /edit/ post ajax request must change UserProfile if its valid"""
        self.client.login(username='admin', password='admin')

        data = user_data.copy()
        data['name'] = 'Nigel'

        response = self.client.post(reverse('edit'), data,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(UserProfile.objects.first().name, data['name'])
        self.assertEquals(json.loads(response.content)['success'], True)

    def test_edit_post_not_ajax_does_not_chane_data(self):
        """/edit/ post not ajax request must change UserProfile if its valid"""
        self.client.login(username='admin', password='admin')

        data = user_data.copy()
        data['name'] = 'Nigel'

        self.client.post(reverse('edit'), data)

        self.assertNotEquals(UserProfile.objects.first().name, data['name'])

    def test_not_logged_in_user_cant_get_edit_page(self):
        """not logged in user getting edit page - redirects '/' """
        response = self.client.get(reverse('edit'))

        self.assertRedirects(response, "%s?next=%s" % (
            reverse('login'), reverse('edit')), 302, 200)

    def test_edit_post_with_invalid_data(self):
        """/edit/ post request with invalid data"""
        self.client.login(username='admin', password='admin')

        data = user_data.copy()
        data['email'] = 'dasdasdasd'

        response = self.client.post(reverse('edit'), data,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEquals(json.loads(response.content)['success'], False)
        self.assertEquals(json.loads(response.content)['err_msg']['email'][0],
                          'Enter a valid email address.')
