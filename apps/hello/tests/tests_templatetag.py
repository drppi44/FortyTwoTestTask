from apps.hello.models import UserProfile
from apps.hello.templatetags.edit_link import edit_link
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class MyTagTest(TestCase):
    """ ticket#8 test: link to edit object in admin """
    def test_link_to_render_object_works(self):
        """ fn returns url to edit object"""
        user = User.objects.first()
        link = edit_link(user)

        self.assertEquals(r'/admin/auth/user/%d/' % user.id, link)

    def test_link_to_render_object_valid_renders_in_html(self):
        """ html has link to edit object"""
        self.client.login(username='admin', password='admin')
        _id = UserProfile.objects.first().id

        response = self.client.get(reverse('index'))

        self.assertIn(r'/admin/hello/userprofile/%d/' % _id, response.content)
