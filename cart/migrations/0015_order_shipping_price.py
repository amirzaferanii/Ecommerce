# Generated by Django 5.0.7 on 2024-08-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_remove_orderitem_shipping_remove_orderitem_sub_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_price',
            field=models.IntegerField(default=0),
        ),
    ]
