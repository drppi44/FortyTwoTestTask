from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField


class UserProfile(models.Model):
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


class ModelSignal(models.Model):
    model = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode('[%s] - %s' % (self.model, self.action))


class MyHttpRequest(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=1000)
    path = models.CharField(max_length=1000)
    method = models.CharField(max_length=50, blank=True, default='')
    uri = models.CharField(max_length=2000)
    query_string = models.CharField(max_length=1000, blank=True)
    is_viewed = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    status_code = models.IntegerField(max_length=3, default='200')

    def __unicode__(self):
        return unicode(self.uri)

    class Meta:
        ordering = ['-priority', '-time']


class Task(models.Model):
    TASK_CHOICE = (
        ('0', 'new'),
        ('1', 'done'),
    )
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices=TASK_CHOICE, max_length=1, default='0')
    user = models.ForeignKey(User)
    position = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['position', '-time']
