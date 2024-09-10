from django.contrib import admin
from .models import Channel


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'eur_amount', 'rub_amount', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Channel, ChannelAdmin)
