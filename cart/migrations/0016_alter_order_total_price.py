# Generated by Django 5.0.7 on 2024-08-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0015_order_shipping_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0, verbose_name='مبلغ کل'),
        ),
    ]
