from django.shortcuts import render
from .models import Order, Product
from django.utils import timezone


def home(request):
    orders = Order.objects.all()
    products = Product.objects.all()

    payment_methods_russian = {
        'non-cash-pay': 'Безналичный расчёт',
        'cash-to-courier': 'наличными курьеру',
    }

    delivery_methods_russian = {
        'self-pickup': 'Самовывоз',
        'courier': 'Курьером',
        'Russian Post': 'Почтой России',
    }

    for order in orders:
        order.payment_method = payment_methods_russian.get(
            order.payment_method, order.payment_method)
        order.delivery_method = delivery_methods_russian.get(
            order.delivery_method, order.delivery_method)

    product_order_numbers = {}
    for product in products:
        orders_with_product = Order.objects.filter(product=product)
        order_numbers = [order.order_number for order in orders_with_product]
        product_order_numbers[product] = order_numbers
        

    context = {
        'orders': orders,
        'products': products,
        'product_order_numbers': product_order_numbers,
    }

    return render(request, 'home.html', context)
