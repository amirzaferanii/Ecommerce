# Generated by Django 5.0.7 on 2024-08-21 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_order_shipping_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shopping',
            new_name='Shipping',
        ),
    ]
