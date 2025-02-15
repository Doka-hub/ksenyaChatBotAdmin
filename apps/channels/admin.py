from django.contrib import admin
from .models import Channel


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'eur_amount', 'rub_amount', 'duration')
    list_editable = ('name', 'url', 'eur_amount', 'rub_amount', 'duration')


admin.site.register(Channel, ChannelAdmin)
