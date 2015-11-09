from .models import ModelSignal
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


@receiver(post_save)
def save_signal(sender, instance, created, **kwargs):
    if isinstance(instance, ModelSignal):
        return
    ModelSignal.objects.create(
        model=instance.__class__.__name__,
        action='creation' if created else 'editing',
    )


@receiver(pre_delete)
def delete_signal(instance, **kwargs):
    ModelSignal.objects.create(
        model=instance.__class__.__name__,
        action='deletion',
    )
