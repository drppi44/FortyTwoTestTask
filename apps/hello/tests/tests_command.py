import StringIO
from django.core import management
from django.db.models import get_models
from django.test import TestCase


class CommandTest(TestCase):
    """ print_models command prints all models """
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
