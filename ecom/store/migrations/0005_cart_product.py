# Generated by Django 5.0.1 on 2024-01-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_cart_products_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(through='store.CartItems', to='store.product'),
        ),
    ]
