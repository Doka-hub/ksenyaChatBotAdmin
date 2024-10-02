from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError
from django.db import connection


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payments'
    verbose_name = 'Платежи'

    def ready(self):
        from . import signals
        from apps.payments.models import RBDetail

        if RBDetail.objects.count() == 0:
            RBDetail.objects.create(
                account_number='1234567890',
                field_1='field1',
                field_2='field2',
            )
