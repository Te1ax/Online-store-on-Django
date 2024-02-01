from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование товара")
    short_description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(verbose_name="Полное описание")
    base_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Базовая цена")
    current_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Текущая цена")
    stock_quantity = models.PositiveIntegerField(verbose_name="Количество на складе")
    sku = models.CharField(max_length=20, verbose_name="Артикул")
    min_order_quantity = models.PositiveIntegerField(verbose_name="Минимальное количество для заказа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class Order(models.Model):
    
    PAYMENT_METHOD_CHOICES = (
        ('non-cash-pay', 'Безналичный расчёт'),
        ('cash-to-courier', 'наличными курьеру'),
    )    
    DELIVERY_METHOD_CHOICES = (
        ('self-pickup', 'Самовывоз'),
        ('courier', 'Курьером'),
        ('Russian Post', 'Почтой России'),
    )    
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Клиент")
    order_number = models.CharField(max_length=20, verbose_name="Номер заказа")
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, verbose_name="Метод оплаты")
    delivery_method = models.CharField(max_length=50, choices=DELIVERY_METHOD_CHOICES, verbose_name="Метод доставки")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    order_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма заказа")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа", editable=False)


    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        
