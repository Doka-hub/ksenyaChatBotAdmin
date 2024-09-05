from django.contrib import admin
from .models import TelegramUser


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'is_blocked', 'role', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_blocked', 'created_at')


admin.site.register(TelegramUser, TelegramUserAdmin)
