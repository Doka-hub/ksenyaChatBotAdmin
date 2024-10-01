from django.db import models

from apps.tgusers.models import TelegramUser


class PaymentType(models.enums.TextChoices):
    EU = 'eur', 'Евро'
    RB = 'rub', 'Белорусский Рубль'


class Payment(models.Model):
    class Meta:
        db_table = 'payment'

    def upload_to(self, filename):
        return f'payments/screenshots/{self.id}/{filename}'

    stripe_id = models.CharField(max_length=255, verbose_name='Номер чека')

    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    type = models.CharField(
        max_length=20,
        choices=PaymentType.choices,
        default=PaymentType.EU,
        verbose_name='Валюта',
    )
    screenshot = models.ImageField(
        upload_to=upload_to,
        null=True,
        blank=True,
        verbose_name='Скриншот',
    )

    is_paid = models.BooleanField(default=False, verbose_name='Оплачен')

    paid_at = models.DateTimeField(null=True, verbose_name='Оплачен (дата)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан (дата)')

    def __str__(self):
        return f'Платеж #{self.id} ({self.user.username})'


class RBDetail(models.Model):
    class Meta:
        db_table = 'rbdetails'

    account_number = models.CharField(max_length=255, verbose_name='Номер счета')
    field_1 = models.CharField(max_length=255, verbose_name='поле 1')
    field_2 = models.CharField(max_length=255, verbose_name='поле 2')
