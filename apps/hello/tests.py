from apps.hello.models import MyData
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from datetime import date


_data = {
    'name': 'Eugene',
    'last_name': 'Shevchenko',
    'date_of_birth': date(1993, 8, 17),
    'bio': 'Django developer',
    'email': 'multinigel@gmail.com',
    'jabber': 'drppi44@jabber.ru',
    'skype': 'drppi44'
}


class HomeViewTest(TestCase):
    """ ticket#1 test: home page with bio """
    fixtures = ['my_fixture.json']

    def test_initial_data_for_admin_load(self):
        """ admin-admin exits in db """
        user = User.objects.first()

        self.assertEquals(user.username, 'admin')
        self.assertTrue(user.check_password('admin'))
        self.assertTrue(user.is_superuser)

    def test_initial_data_load(self):
        """ my data exits in db (name,last_name,bio....) """
        data = MyData.objects.first()

        for key in _data.keys():
            self.assertEquals(_data[key], getattr(data, key))

    def test_home_view_template_uses_right_template(self):
        """ index_view using right template """

        response = self.client.get(reverse('index'))

        self.assertTemplateUsed(response, 'index.html')

    def test_data_in_home_view_equals_data_io_db(self):
        """ data send to template is valid """
        response = self.client.get(reverse('index'))
        data = MyData.objects.first()

        self.assertEquals(response.context['data'], data)

    def test_db_contains_one_data_entity(self):
        """bd must contain 1 mydata instance"""
        count = MyData.objects.count()

        self.assertEquals(count, 1)

    def test_home_html_renders_with_data(self):
        """rendered html page should contain mydata"""
        response = self.client.get(reverse('index'))

        for value in _data.values():
            if isinstance(value, date):
                value = value.strftime("%b. %d, %Y")
            self.assertIn(value, response.content)
