from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.payments'
    verbose_name = 'Платежи'

    def ready(self):
        from . import signals
        from apps.payments.models import RBDetail

        if RBDetail.objects.count() == 0:
            RBDetail.objects.create(
                text='text',
            )
