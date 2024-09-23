from django.db import models


class TelegramUserRole(models.enums.TextChoices):
    CLIENT = 'CLIENT', 'Клиент'
    MANAGER = 'MANAGER', 'Менеджер'


class TelegramUser(models.Model):
    user_id = models.CharField(max_length=255, verbose_name='ТГ юзер айди')
    username = models.CharField(max_length=30, verbose_name='Ник пользователя')
    first_name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия пользователя')
    phone_number = models.CharField(max_length=30, null=True, blank=True, verbose_name='Номер телефона пользователя')
    email = models.EmailField(verbose_name='Почта')
    is_blocked = models.BooleanField(verbose_name='Заблокировал Бота')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    role = models.CharField(
        max_length=20,
        choices=TelegramUserRole.choices,
        verbose_name='Роль'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'


class StartMessage(models.Model):
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    image = models.ImageField(verbose_name='Изображние', upload_to='images/', blank=True, null=True)
    video = models.FileField(verbose_name='Видео' ,upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
