from django.contrib import admin
from .models import Payment, RBPaymentDetail


def mark_as_paid(modeladmin, request, queryset):
    queryset.update(is_paid=True)


mark_as_paid.short_description = "Mark selected payments as paid"


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'stripe_id', 'amount', 'is_paid', 'type', 'created_at')
    search_fields = ('user__username', 'stripe_id')
    list_filter = ('is_paid', 'type', 'created_at')
    actions = [mark_as_paid]


class RBPaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'field1', 'field2')
    search_fields = ('account_number', 'field1', 'field2')
    list_filter = ('account_number', 'field1', 'field2')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Payment, PaymentAdmin)
admin.site.register(RBPaymentDetail, RBPaymentDetailsAdmin)
