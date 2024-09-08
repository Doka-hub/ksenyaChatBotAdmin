from django.db import models
from apps.tgusers.models import TelegramUser


class PaymentType(models.enums.TextChoices):
    EU = 'EU', 'EU'
    RB = 'RB', 'RB'


class Payment(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    stripe_id = models.CharField(max_length=255, verbose_name='Номер чека')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество')
    is_paid = models.BooleanField(default=False, verbose_name='оплата заказа')
    type = models.CharField(
        max_length=20,
        choices=PaymentType.choices,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} --- {self.is_paid}'


class PaymentDetails(models.Model):
    value = models.CharField(max_length=100, verbose_name='Значение')

    def __str__(self):
        return f'{self.value}'


class RBPaymentDetails(models.Model):
    account_id = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    field1 = models.CharField(max_length=255, verbose_name='поле 1')
    field2 = models.CharField(max_length=255, verbose_name='поле 2')
