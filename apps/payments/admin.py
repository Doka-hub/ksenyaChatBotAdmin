from django.contrib import admin
from django.utils.html import format_html

from .models import Payment, RBDetail


def mark_as_paid(modeladmin, request, queryset):
    queryset.update(is_paid=True)


mark_as_paid.short_description = "Mark selected payments as paid"


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'stripe_id', 'amount', 'is_paid', 'type', 'created_at')
    search_fields = ('user__username', 'stripe_id')
    list_filter = ('is_paid', 'type', 'created_at')
    actions = (mark_as_paid,)

    readonly_fields = (
        'user',
        'amount',
        'type',
        'stripe_id',
        'created_at',
        'screenshot',
    )
    fieldsets = (
        (
            'Инфо', {
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
            'Статусы', {
                'fields': (
                    'screenshot',
                    'is_paid',
                )
            },
        ),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def display_screenshot(self, obj):
        if obj.payment_screenshot:
            return format_html(
                '<img src="{}" width="150" height="150" />',
                obj.payment_screenshot.url
            )
        return "No screenshot available"

    display_screenshot.short_description = 'Payment Screenshot'


class RBDetailsAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'field1', 'field2')
    search_fields = ('account_number', 'field1', 'field2')
    list_filter = ('account_number', 'field1', 'field2')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Payment, PaymentAdmin)
admin.site.register(RBDetail, RBDetailsAdmin)
