import requests
from django.contrib import admin

from apps.tgusers.models import TelegramUser
from apps.utils.admin import BotDBModelAdmin, BotDBStackedInline, BotDBTabularInline
from .models import (
    Notification,
    NotificationButton,
    NotificationImage,
    UsersNotifications,
)


class TGUsersNotificationInline(BotDBTabularInline):
    model = UsersNotifications
    extra = 1
    readonly_fields = ['delivered_time']

    def get_field_queryset(self, db, db_field, request):
        """
            Фильтрует только активных пользователей
        :param db:
        :param db_field:
        :param request:
        :return:
        """
        related_admin = self.admin_site._registry.get(db_field.remote_field.model)
        ordering = related_admin.get_ordering(request)
        if db_field.name == 'user':
            return TelegramUser.objects.filter(is_active=True, is_bot_blocked=False).order_by(
                *ordering
            )


class NotificationButtonInline(BotDBStackedInline):
    model = NotificationButton
    extra = 0


class NotificationImageInline(BotDBStackedInline):
    model = NotificationImage
    extra = 0


class NotificationAdmin(BotDBModelAdmin):
    list_display = ['id', 'title']
    exclude = ['file', 'filters']
    inlines = [NotificationButtonInline, NotificationImageInline, TGUsersNotificationInline]

    def title(self, obj: Notification):
        return obj.text.split(' ')[0] if obj.text else ''

    title.short_description = 'Название'

    def get_inlines(self, request, obj):
        if request.method == 'POST':
            inlines = self.inlines
        else:
            inlines = [NotificationButtonInline, NotificationImageInline]
        return inlines
    def save_model(self, request, obj: Notification, form, change):
        if not obj.pk:
            obj.save(using=self.using)

        if obj.send_all or obj.send_separately:
            data = {
                'type': 'default',
                'notification_id': obj.id,
                'message': obj.text,
                'buttons': [
                    {
                        'name': button.text,
                        'url': button.url,
                    } for button in obj.buttons.all()
                ],
                'images': [
                    'https://bot.chertovich.com' + image.image.url for image in obj.images.all()
                ],
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
