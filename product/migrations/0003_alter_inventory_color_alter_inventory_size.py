# Generated by Django 5.0.7 on 2024-08-18 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_color_remove_product_size_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.color', verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.size', verbose_name='سایز'),
        ),
    ]
