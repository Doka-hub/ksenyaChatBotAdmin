from django.db import models


class TelegramUserRole(models.enums.TextChoices):
    CLIENT = 'CLIENT', 'Клиент'
    MANAGER = 'MANAGER', 'Менеджер'


class TelegramUser(models.Model):
    class Meta:
        db_table = 'tguser'
        verbose_name = 'ТГ Пользователь'
        verbose_name_plural = 'ТГ Пользователи'

    user_id = models.CharField(max_length=255, verbose_name='Telegram ID')
    username = models.CharField(max_length=30, blank=True, null=True, verbose_name='Никейм')

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='Фамилия',
    )

    phone_number = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='Номер Телефона',
    )
    email = models.EmailField(blank=True, null=True, verbose_name='Почта')

    is_bot_blocked = models.BooleanField(verbose_name='Заблокировал Бота')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    role = models.CharField(
        max_length=20,
        choices=TelegramUserRole.choices,
        verbose_name='Роль'
    )

    def __str__(self):
        return self.username or self.first_name or self.user_id


class StartMessage(models.Model):
    class Meta:
        db_table = 'startmessage'

        verbose_name = 'Приветсвенное Сообщение'
        verbose_name_plural = 'Приветсвенное Сообщение'

    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    photo = models.ImageField(verbose_name='Изображние', upload_to='images/', blank=True, null=True)
    video = models.FileField(verbose_name='Видео', upload_to='videos/', blank=True, null=True)

    def get_photo_url(self):
        if self.photo:
            photo_url = 'https://bot.chertovich.com' + self.photo.url
        else:
            photo_url = None
        return photo_url

    def get_video_url(self):
        if self.video:
            video_url = 'https://bot.chertovich.com' + self.video.url
        else:
            video_url = None
        return video_url

    def __str__(self):
        return 'Приветсвенное сообщение'
