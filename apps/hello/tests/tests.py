import StringIO
from ..templatetags.edit_link import edit_link
from ..models import MyHttpRequest
from django.core import management
from django.db.models import get_models
from apps.hello.models import UserProfile, ModelSignal
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
    fixtures = ['user_data.json']

    def test_initial_data_for_admin_load(self):
        """ admin-admin exits in db """
        user = User.objects.first()

        self.assertEquals(user.username, 'admin')
        self.assertTrue(user.check_password('admin'))
        self.assertTrue(user.is_superuser)

    def test_initial_data_load(self):
        """ my data exits in db (name,last_name,bio....) """
        data = UserProfile.objects.first()

        for key in _data.keys():
            self.assertEquals(_data[key], getattr(data, key))

    def test_home_view_template_uses_right_template(self):
        """ index_view using right template """

        response = self.client.get(reverse('index'))

        self.assertTemplateUsed(response, 'index.html')

    def test_data_in_home_view_equals_data_io_db(self):
        """ data send to template is valid """
        response = self.client.get(reverse('index'))
        data = UserProfile.objects.first()

        self.assertEquals(response.context['data'], data)

    def test_db_contains_one_data_entity(self):
        """bd must contain 1 UserProfile instance"""
        count = UserProfile.objects.count()

        self.assertEquals(count, 1)

    def test_home_html_renders_with_data(self):
        """rendered html page should contain UserProfile"""
        response = self.client.get(reverse('index'))

        for value in _data.values():
            if isinstance(value, date):
                value = value.strftime("%b. %d, %Y")
            self.assertIn(value, response.content)


class MyTagTest(TestCase):
    """ ticket#8 test: link to edit object in admin """
    fixtures = ['user_data.json']

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


class CommandTest(TestCase):
    """ print_models command prints all models """
    fixtures = ['user_data.json']

    def test_command_prints_models_names(self):
        """ command prints all models """
        out = StringIO.StringIO()
        management.call_command('print_models', stdout=out)

        models = get_models()
        for model in models:
            self.assertIn(model.__name__, out.getvalue())

    def test_command_prints_models_count(self):
        """ command prints all models count and each count """
        out = StringIO.StringIO()
        management.call_command('print_models', stdout=out)

        models = get_models()
        for model in models:
            self.assertIn(
                '[%s] - %d' % (model.__name__, model._default_manager.count()),
                out.getvalue())


class ModelSignalTest(TestCase):
    fixtures = ['user_data.json']

    def test_signal_edit_works(self):
        """editing any model saves in db"""
        profile = UserProfile.objects.first()
        profile.name = 'John'
        profile.save()

        entity = ModelSignal.objects.last()

        self.assertEquals(entity.model, UserProfile.__name__)
        self.assertEquals(entity.action, 'editing')

    def test_signal_create_works(self):
        """creating any model saves in db"""
        User.objects.create(username='asdasd', password='asdasd')

        entity = ModelSignal.objects.last()

        self.assertEquals(entity.model, User.__name__)
        self.assertEquals(entity.action, 'creation')

    def test_signal_delete_works(self):
        """deleting any model saves in db"""
        self.client.get(reverse('index'))
        MyHttpRequest.objects.last().delete()

        entity = ModelSignal.objects.last()

        self.assertEquals(entity.model, MyHttpRequest.__name__)
        self.assertEquals(entity.action, 'deletion')
