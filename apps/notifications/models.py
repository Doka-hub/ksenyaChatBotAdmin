from django.db import models

from apps.tgusers.models import TelegramUser


class Notification(models.Model):
    def upload_to(self, filename):
        return f'notifications/notification_{self.id}/{filename}'

    users = models.ManyToManyField(
        TelegramUser,
        related_name='notifications',
        through='UsersNotifications',
        verbose_name='ТГ Пользователи',
    )
    # image = models.ImageField(
    #     verbose_name='Изображение',
    #     upload_to=upload_to,
    #     blank=True,
    #     null=True,
    # )
    # file = models.FileField(verbose_name='Файл', upload_to=upload_to, blank=True, null=True)

    text = models.TextField(verbose_name='Текст')

    send_separately = models.BooleanField(default=False, verbose_name='Отправить в отдельности')
    send_all = models.BooleanField(default=False, verbose_name='Отправить всем')

    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        db_table = 'notification'
        verbose_name = 'Уведомление для Пользователя'
        verbose_name_plural = 'Уведомления для Пользователей'

    def __str__(self):
        return f'Уведомление #{self.id}'


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
