from apps.hello.models import MyHttpRequest
from apps.hello.models import UserProfile, ModelSignal
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class ModelSignalTest(TestCase):
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
