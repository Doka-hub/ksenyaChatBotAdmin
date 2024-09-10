from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError
from django.db import connection


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payments'

    def ready(self):
        from . import signals
