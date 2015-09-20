from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django_resized import ResizedImageField
from datetime import datetime
from functools import wraps


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


class ModelSignal(models.Model):
    model = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode('[%s] - %s' % (self.model, self.action))


def disable_for_loaddata(signal_handler):
    """
    Decorator that turns off signal handlers when loading fixture data.
    """

    @wraps(signal_handler)
    def wrapper(*args, **kwargs):
        from django.db import connection
        if 'hello_modelsignal' not in connection.introspection.table_names():
            return
        signal_handler(*args, **kwargs)
    return wrapper


@receiver(pre_save)
@disable_for_loaddata
def save_signal(instance, **kwargs):
    date = datetime.now()
    if not isinstance(instance, ModelSignal):
        ModelSignal.objects.create(
            model=instance.__class__.__name__,
            action='editing' if hasattr(instance, 'id') else 'creation',
            date=date
        )


@receiver(pre_delete)
def delete_signal(instance, **kwargs):
    date = datetime.now()
    ModelSignal.objects.create(
        model=instance.__class__.__name__,
        action='deletion',
        date=date
    )
