from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = ('id', 'created',
              ('first_name', 'telefon'),
              ('email', 'location'),
              'basket_history', 'status', 'initiator')
    readonly_fields = ('id', 'created')