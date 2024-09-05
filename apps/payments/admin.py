from django.contrib import admin
from .models import Payment, PaymentDetails


def mark_as_paid(modeladmin, request, queryset):
    queryset.update(is_paid=True)


mark_as_paid.short_description = "Mark selected payments as paid"


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'stripe_id', 'amount', 'is_paid', 'type', 'created_at')
    search_fields = ('user__username', 'stripe_id')
    list_filter = ('is_paid', 'type', 'created_at')
    actions = [mark_as_paid]


class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('value',)


admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentDetails, PaymentDetailsAdmin)
