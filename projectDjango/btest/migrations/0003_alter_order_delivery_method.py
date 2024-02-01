# Generated by Django 4.2.7 on 2024-01-25 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0002_alter_customer_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('self-pickup', 'Самовывоз'), ('courier', 'Курьером'), ('Russian Post', 'Почтой России')], max_length=50, verbose_name='Метод доставки'),
        ),
    ]