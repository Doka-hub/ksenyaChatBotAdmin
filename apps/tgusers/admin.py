from django.contrib import admin
from .models import TelegramUser, StartMessage
from django.core.exceptions import ValidationError


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'is_blocked', 'role', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_blocked', 'created_at')

    def has_add_permission(self, request):
        return False


class StartMessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'image', 'video', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        new_image = form.cleaned_data.get('image')
        new_video = form.cleaned_data.get('video')

        if (new_image and obj.video) or (new_video and obj.image):
            form.add_error(None, ValidationError("Должно быть заполнено только одно поле: изображение или видео."))
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
