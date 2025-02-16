from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.html import format_html

from .models import TelegramUser, StartMessage, ButtonMessage


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

        'policy_confirmed',

        'is_bot_blocked',
        'is_active',
    )
    search_fields = ('username', 'email')
    list_filter = ('role', 'policy_confirmed', 'is_bot_blocked', 'is_active')

    readonly_fields = (
        'policy_confirmed',
    )

    fieldsets = (
        (
            'Info', {
                'fields': (
                    'phone_number',
                    'email',
                    'role',
                ),
            },
        ),
        (
            'TG Info', {
                'fields': (
                    'user_id',
                    'username',

                    'first_name',
                    'last_name',

                    'policy_confirmed',

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

class ButtonMessageAdmin(admin.StackedInline):
    model = ButtonMessage
    extra = 0
    fields = (
        'type',
        'name',
        'url',
        'callback_data',
    )


class StartMessageAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'photo',
        'video',
    )
    inlines = (ButtonMessageAdmin,)
    
    def save_model(self, request, obj, form, change):
        new_image = form.cleaned_data.get('photo')
        new_video = form.cleaned_data.get('video')

        if (new_image and obj.video) or (new_video and obj.photo):
            raise ValidationError('Должно быть заполнено только одно поле: изображение или видео.')

        super().save_model(request, obj, form, change)


admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(StartMessage, StartMessageAdmin)
