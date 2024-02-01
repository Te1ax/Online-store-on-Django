# Generated by Django 4.2.7 on 2024-01-22 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя клиента'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btest.customer', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('pickup', 'Самовывоз'), ('courier', 'Курьером'), ('Russian Post', 'Почтой России')], max_length=50, verbose_name='Метод доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=20, verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('non-cash-pay', 'Безналичный расчёт'), ('cash-to-courier', 'наличными курьеру')], max_length=50, verbose_name='Метод оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btest.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='base_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Базовая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='current_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Текущая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='full_description',
            field=models.TextField(verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='min_order_quantity',
            field=models.PositiveIntegerField(verbose_name='Минимальное количество для заказа'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=20, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.PositiveIntegerField(verbose_name='Количество на складе'),
        ),
    ]