from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin.actions import delete_selected

from .models import Payment, RBDetail, Subscription


def mark_as_paid(modeladmin, request, queryset):
    queryset.update(is_paid=True)


mark_as_paid.short_description = "Mark selected payments as paid"


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'stripe_id', 'amount', 'is_paid', 'type', 'created_at')
    search_fields = ('user__username', 'stripe_id')
    list_filter = ('is_paid', 'type', 'created_at')
    actions = (delete_selected, mark_as_paid,)

    readonly_fields = (
        'user',
        'amount',
        'type',
        'stripe_id',
        'created_at',
        'screenshot',
        'paid_at',
        'display_screenshot',
    )
    fieldsets = (
        (
            'Info', {
                'fields': (
                    'user',
                    'amount',
                    'type',
                    'created_at',
                ),
            },
        ),
        (
            'Stipe', {
                'fields': (
                    'stripe_id',
                )
            },
        ),
        (
            'Statuses', {
                'fields': (
                    'display_screenshot',
                    'paid_at',
                    'is_paid',
                )
            },
        ),
    )

    def has_add_permission(self, request):
        return False

    def display_screenshot(self, obj: Payment):
        if obj.screenshot:
            return format_html(
                '<a href="{url}" target="_blank"><img src="{url}" width="150" height="150" /></a>',
                url=obj.screenshot.url,
            )
        return "No screenshot available"

    display_screenshot.short_description = 'Payment Screenshot'


class RBDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'channel', 'created_at', 'active_by')
    search_fields = ('user',)

    def has_add_permission(self, request):
        return False


admin.site.register(Payment, PaymentAdmin)
admin.site.register(RBDetail, RBDetailAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
