from django.shortcuts import render
from .models import Order, Product
from django.http import HttpResponse

def home(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    context = {
        'orders': orders,
        'products': products,
    }
    return render(request, 'home.html', context)

def index(request):
    return HttpResponse("Привет! Это твое первое приложение!")
