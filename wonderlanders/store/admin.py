from django.contrib import admin

from wonderlanders.store.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'order_date'
                    , 'user', 'order_products_quantity', 'order_total_price', )
