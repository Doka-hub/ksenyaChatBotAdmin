from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError
from django.db import connection


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payments'

    def ready(self):
        from . import signals
        from apps.payments.models import RBDetail

        if RBDetail.objects.count() == 0:
            RBPaymentDetail.objects.create(
                account_number='1234567890',
                field1='field1',
                field2='field2',
            )
