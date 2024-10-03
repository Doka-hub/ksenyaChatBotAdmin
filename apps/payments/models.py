from datetime import datetime

from django.db import models

from apps.channels.models import Channel
from apps.tgusers.models import TelegramUser


class PaymentType(models.enums.TextChoices):
    EU = 'eur', 'Евро'
    RB = 'rub', 'Белорусский Рубль'


class Payment(models.Model):
    class Meta:
        db_table = 'payment'

        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

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
        return f'Платеж #{self.id} ({self.user})'


class RBDetail(models.Model):
    class Meta:
        db_table = 'rbdetails'

        verbose_name = 'Детали РБ Счета'
        verbose_name_plural = 'Детали РБ Счета'

    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return 'Платежи РБ Счета'


class Subscription(models.Model):
    class Meta:
        db_table = 'subscription'

        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    payment = models.OneToOneField(
        Payment,
        related_name='subscription',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(TelegramUser, related_name='subscriptions', on_delete=models.CASCADE)
    channel = models.ForeignKey(
        Channel,
        related_name='subscriptions',
        on_delete=models.SET_NULL,
        null=True,
    )

    created_at = models.DateTimeField(default=datetime.now)
    active_by = models.DateTimeField(null=True)

    def __str__(self):
        return f'Подписка #{self.id} ({self.user})'
