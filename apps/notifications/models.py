from django.db import models

from apps.tgusers.models import TelegramUser


class Notification(models.Model):
    def upload_to(self, filename):
        return f'notifications/notification_{self.id}/{filename}'

    class Filters(models.TextChoices):
        ALL = 'ALL', 'Всем'
        TEST = 'TEST', 'Тест'

    users = models.ManyToManyField(
        TelegramUser,
        related_name='notifications',
        through='UsersNotifications',
        verbose_name='ТГ Пользователи',
    )

    text = models.TextField(verbose_name='Текст')

    filters = models.CharField(
        max_length=255,
        choices=Filters.choices,
        default=Filters.ALL,
        verbose_name='Фильтры',
    )
    send_separately = models.BooleanField(default=False, verbose_name='Отправить в отдельности')
    send_all = models.BooleanField(default=False, verbose_name='Отправить всем')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        db_table = 'notification'
        verbose_name = 'Уведомление для Пользователя'
        verbose_name_plural = 'Уведомления для Пользователей'

    def __str__(self):
        return f'Уведомление #{self.id}'


class NotificationButton(models.Model):
    class Meta:
        db_table = 'notificationbutton'

    notification = models.ForeignKey(
        Notification,
        models.CASCADE,
        related_name='buttons',
        verbose_name='Уведомление',
    )
    text = models.CharField(max_length=255, verbose_name='Текст')
    url = models.URLField(null=True, blank=True, verbose_name='Ссылка')


class NotificationImage(models.Model):
    class Meta:
        db_table = 'notificationimage'

    notification = models.ForeignKey(
        Notification,
        models.CASCADE,
        related_name='images',
        verbose_name='Уведомление',
    )
    image = models.ImageField(upload_to='notifications', verbose_name='Картинка')


class UsersNotifications(models.Model):
    user = models.ForeignKey(TelegramUser, models.CASCADE, related_name='users_notifications')
    notification = models.ForeignKey(
        Notification,
        models.CASCADE,
        related_name='users_notifications',
    )
    delivered = models.BooleanField(default=False, verbose_name='Доставлено')
    delivered_time = models.DateTimeField(null=True, verbose_name='Доставлено (дата)')

    class Meta:
        db_table = 'usersnotifications'

    def __str__(self):
        return str(self.user)
