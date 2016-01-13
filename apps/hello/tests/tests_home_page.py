from apps.hello.models import UserProfile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from datetime import date


user_data = dict(
    name='Eugene',
    last_name='Shevchenko',
    date_of_birth=date(1993, 8, 17),
    bio='Django developer',
    email='multinigel@gmail.com',
    jabber='drppi44@jabber.ru',
    skype='drppi44'
)


class TestNoData(TestCase):
    def test_error_msg_if_no_data(self):
        """error message on home page if no user_data in db"""
        UserProfile.objects.first().delete()
        response = self.client.get(reverse('index1'))

        self.assertIn("Error: No data", response.content)


class HomeViewTest(TestCase):
    """ ticket#1 test: home page with bio """
    def test_initialuser_data_for_admin_load(self):
        """ admin-admin exits in db """
        user = User.objects.first()

        self.assertEquals(user.username, 'admin')
        self.assertTrue(user.check_password('admin'))
        self.assertTrue(user.is_superuser)

    def test_initialuser_data_load(self):
        """ my data exits in db (name,last_name,bio....) """
        data = UserProfile.objects.first()

        for key in user_data.keys():
            self.assertEquals(user_data[key], getattr(data, key))

    def test_home_view_template_uses_right_template(self):
        """ index_view using right template """

        response = self.client.get(reverse('index'))

        self.assertTemplateUsed(response, 'hello/index.html')

    def testuser_data_in_home_view_equalsuser_data_io_db(self):
        """ data send to template is valid """
        response = self.client.get(reverse('index'))
        data = UserProfile.objects.first()

        self.assertEquals(response.context['data'], data)

    def test_db_contains_oneuser_data_entity(self):
        """bd must contain 1 UserProfile instance"""
        count = UserProfile.objects.count()

        self.assertEquals(count, 1)

    def test_home_html_renders_withuser_data(self):
        """rendered html page should contain UserProfile"""
        response = self.client.get(reverse('index'))

        for value in user_data.values():
            if isinstance(value, date):
                value = value.strftime("%b. %d, %Y")
            self.assertIn(value, response.content)
