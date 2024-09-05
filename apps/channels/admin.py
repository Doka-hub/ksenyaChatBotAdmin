from django.contrib import admin
from .models import Channel


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'amount', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


admin.site.register(Channel, ChannelAdmin)
