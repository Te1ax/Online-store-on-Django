# Generated by Django 4.2.7 on 2023-11-13 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('full_description', models.TextField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock_quantity', models.PositiveIntegerField()),
                ('sku', models.CharField(max_length=20)),
                ('min_order_quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20)),
                ('payment_method', models.CharField(max_length=50)),
                ('delivery_method', models.CharField(max_length=50)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btest.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btest.product')),
            ],
        ),
    ]
