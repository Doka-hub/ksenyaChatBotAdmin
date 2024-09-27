from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.html import format_html

from .models import TelegramUser, StartMessage


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'role',

        'username',
        'username_link',

        'first_name',
        'last_name',

        'phone_number',
        'email',

        'is_bot_blocked',
        'is_active',
    )
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_bot_blocked')

    fieldsets = (
        (
            'Инфо', {
                'fields': (
                    'phone_number',
                    'email',
                    'role',
                ),
            },
        ),
        (
            'ТГ Инфо', {
                'fields': (
                    'user_id',
                    'username',

                    'first_name',
                    'last_name',

                    'is_bot_blocked',
                    'is_active',
                )
            },
        ),
    )

    def username_link(self, obj: TelegramUser):
        if obj.username:
            url = f'https://t.me/{obj.username}/'
            target = '_blank'
            username = format_html(
                '<a href="{}" target="{}" style="font-size: 10px!important">перейти</a>',
                url,
                target,
            )
        else:
            username = '-'

        return username

    username_link.short_description = '(ТГ ссылка)'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class StartMessageAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'photo',
        'video',
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        new_image = form.cleaned_data.get('image')
        new_video = form.cleaned_data.get('video')

        if (new_image and obj.video) or (new_video and obj.image):
            form.add_error(
                None,
                ValidationError("Должно быть заполнено только одно поле: изображение или видео.")
            )
            return

        if new_video:
            if obj.image:
                obj.image.delete(save=False)
                obj.image = None

        if new_image:
            if obj.video:
                obj.video.delete(save=False)
                obj.video = None

        super().save_model(request, obj, form, change)

    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')

        if (image and video) or (not image and not video):
            raise ValidationError("Должно быть заполнено только одно поле: изображение или видео.")

        return cleaned_data


admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(StartMessage, StartMessageAdmin)
