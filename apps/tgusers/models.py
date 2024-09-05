from django.db import models


class TelegramUserRole(models.enums.TextChoices):
    CLIENT = 'CLIENT', 'Клиент'
    MANAGER = 'MANAGER', 'Менеджер'


class TelegramUser(models.Model):
    username = models.CharField(max_length=30, verbose_name='Ник пользователя')
    first_name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия пользователя')
    phone_number = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона пользователя')
    email = models.EmailField(verbose_name='')
    is_blocked = models.BooleanField()
    role = models.CharField(
        max_length=20,
        choices=TelegramUserRole.choices,
        verbose_name='Роль'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'
