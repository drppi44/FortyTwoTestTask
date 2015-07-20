from apps.hello.models import MyData
from django.contrib.auth.models import User
from django.test import TestCase
from datetime import date


class HomeViewTest(TestCase):
    """ ticket#1 test: home page with bio """
    def test_initial_data_admin(self):
        """
        admin-admin exits in db
        """
        user = User.objects.first()

        self.assertEquals(user.username, 'admin')
        self.assertTrue(user.check_password('admin'))
        self.assertTrue(user.is_superuser)

    def test_initial_data_mydata(self):
        """
        my data exits in db (name,last_name,bio....)
        """
        data = MyData.objects.first()

        _data = {
            'name': 'Eugene',
            'last_name': 'Shevchenko',
            'date_of_birth': date(1993, 8, 17),
            'bio': 'Django developer',
            'email': 'multinigel@gmail.com',
            'jabber': 'drppi44@jabber.ru',
            'skype': 'drppi44'
        }

        for key in _data.keys():
            self.assertEquals(_data[key], getattr(data, key))

