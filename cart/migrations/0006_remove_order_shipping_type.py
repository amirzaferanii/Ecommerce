# Generated by Django 5.0.7 on 2024-08-21 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_rename_shopping_shipping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping_type',
        ),
    ]