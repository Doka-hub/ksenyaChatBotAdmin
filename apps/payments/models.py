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
    paid_at = models.DateTimeField(null=True)
    type = models.CharField(
        max_length=20,
        choices=PaymentType.choices,
    )
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} --- {self.is_paid}'


class RBPaymentDetail(models.Model):
    account_number = models.CharField(max_length=255, verbose_name='Номер счета')
    field1 = models.CharField(max_length=255, verbose_name='поле 1')
    field2 = models.CharField(max_length=255, verbose_name='поле 2')
