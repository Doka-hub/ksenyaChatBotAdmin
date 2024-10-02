from django.contrib import admin
from .models import Channel


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'eur_amount', 'rub_amount', 'duration')
    list_editable = ('name', 'url', 'eur_amount', 'rub_amount', 'duration')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Channel, ChannelAdmin)
