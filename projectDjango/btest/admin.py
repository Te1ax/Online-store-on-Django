from django.contrib import admin
from .models import Product, Customer, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_price', 'stock_quantity', 'min_order_quantity')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer', 'product', 'order_total', 'order_date', 'payment_method', 'delivery_method')

    def get_products_display(self, obj):
        return obj.product.name  # Отображайте только имя продукта

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
