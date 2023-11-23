from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    full_description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    sku = models.CharField(max_length=20)
    min_order_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    delivery_method = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number
