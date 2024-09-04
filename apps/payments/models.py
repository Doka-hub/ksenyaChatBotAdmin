from django.db import models
from apps.tgusers.models import TelegramUser


class PaymentType(models.enums.TextChoices):
    EU = 'EU', 'EU'
    RB = 'RB', 'RB'


class Payment(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=255, verbose_name='Номер чека')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество')
    is_paid = models.BooleanField(default=False, verbose_name='оплата заказа')
    type = models.CharField(
        max_length=20,
        choices=PaymentType.choices,
    )

    def __str__(self):
        return f'{self.user.username} --- {self.is_paid}'


class PaymentDetails(models.Model):
    value = models.CharField(max_length=100, verbose_name='Значение')

    def __str__(self):
        return f'{self.value}'
