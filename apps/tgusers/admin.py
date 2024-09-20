from django.contrib import admin
from .models import TelegramUser, StartMessage


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'is_blocked', 'role', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_blocked', 'created_at')

    def has_add_permission(self, request):
        return False


class StartMessageAdmin(admin.ModelAdmin):
    list_display = ('start_message', 'text', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(StartMessage, StartMessageAdmin)
