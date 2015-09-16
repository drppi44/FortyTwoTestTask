from django.db import models
from django_resized import ResizedImageField


class MyData(models.Model):
    name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    jabber = models.CharField(max_length=255, blank=True)
    skype = models.CharField(max_length=255, blank=True)
    other_contacts = models.TextField(blank=True)
    avatar = ResizedImageField(
        size=[200, 200],
        blank=True,
        upload_to='avatar',
        max_length=255,
        default=''
    )

    def __unicode__(self):
        return unicode(self.name)
