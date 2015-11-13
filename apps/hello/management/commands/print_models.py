from django.core.management.base import BaseCommand
from django.db.models import get_models


class Command(BaseCommand):
    help = 'Print all ContentType models and each count'

    def handle(self, *args, **options):
        for model in get_models():
            line = '[%s] - %d objects' % (
                model.__name__, model._default_manager.count())
            self.stdout.write(line)
            self.stderr.write('error: '+line)
