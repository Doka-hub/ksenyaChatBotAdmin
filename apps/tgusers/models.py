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

    policy_confirmed = models.BooleanField(default=False, verbose_name='Подтвердил Политику Конф')

    is_bot_blocked = models.BooleanField(verbose_name='Заблокировал Бота')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    role = models.CharField(
        max_length=20,
        choices=TelegramUserRole.choices,
        verbose_name='Роль'
    )

    def __str__(self):
        return self.username or self.first_name or self.user_id


class ButtonMessage(models.Model):
    class Meta:
        db_table = 'buttonmessage'

        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'

    class Type(models.TextChoices):
        INLINE = 'INLINE', 'Inline'
        KEYBOARD = 'KEYBOARD', 'Keyboard'

    type = models.CharField(choices=Type.choices, verbose_name='Тип', max_length=10)
    name = models.CharField(max_length=255, verbose_name='Название')
    url = models.URLField(blank=True, null=True, verbose_name='Ссылка')
    callback_data = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Callback Data',
    )

    def __str__(self):
        return f'{self.type} кнопка: {self.name}'


class StartMessageButton(models.Model):
    class Meta:
        db_table = 'startmessagebutton'

        verbose_name = 'Кнопка Стартового Сообщения'
        verbose_name_plural = 'Кнопки Стартового Сообщения'

    message = models.ForeignKey(
        'StartMessage',
        on_delete=models.CASCADE,
        related_name='buttons',
        verbose_name='Сообщение',
    )
    button = models.ForeignKey(
        ButtonMessage,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Кнопка',
    )

    def __str__(self):
        return f'{self.message} - {self.button}'


class StartMessage(models.Model):
    class Meta:
        db_table = 'startmessage'

        verbose_name = 'Приветсвенное Сообщение'
        verbose_name_plural = 'Приветсвенное Сообщение'

    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    photo = models.ImageField(verbose_name='Изображние', upload_to='images/', blank=True, null=True)
    video = models.FileField(verbose_name='Видео', upload_to='videos/', blank=True, null=True)
    buttons = models.ManyToManyField(
        ButtonMessage,
        through=StartMessageButton,
        verbose_name='Кнопки',
        blank=True,
    )

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
