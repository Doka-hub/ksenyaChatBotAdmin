from django.contrib import admin

import requests

from apps.tgusers.models import TelegramUser
from apps.utils.admin import BotDBModelAdmin
from .models import (
    Notification,
    UsersNotifications,
)


class NotificationAdmin(BotDBModelAdmin):
    list_display = ['id', 'users_ids']
    exclude = ['file']

    def users_ids(self, obj: Notification):
        return [user.id for user in obj.users.all()]

    def save_model(self, request, obj: Notification, form, change):
        if not obj.pk:
            obj.save(using=self.using)

        if obj.send_all or obj.send_separately:
            data = {
                'type': 'default',
                'notification_id': obj.id,
                'message': obj.text,
            }

            if obj.send_all:
                users_to_notify = []
                for tg_user in TelegramUser.objects.filter(
                        is_active=True,
                        is_bot_blocked=False
                ).exclude(
                        users_notifications__notification=obj,
                ):
                    users_to_notify.append(
                        UsersNotifications(
                            notification_id=obj.id,
                            user_id=tg_user.id,
                        ),
                    )

                obj.users_notifications.bulk_create(users_to_notify)

            data.update(
                {
                    'users_ids': list(
                        map(
                            lambda tg_user: (
                                tg_user['id'],
                                tg_user['user_id'],
                            ),
                            obj.users.filter(users_notifications__delivered=False).values(
                                'id',
                                'user_id',
                            ),
                        ),
                    ),
                }
            )
            requests.post('http://backend:8000/api/notifications/', json=data)

            obj.send_separately = False
            obj.send_all = False

        obj.save(using=self.using)


admin.site.register(Notification, NotificationAdmin)
