# Generated by Django 5.0.7 on 2024-08-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_color_remove_product_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, to='product.color', verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, to='product.size', verbose_name='سایز'),
        ),
    ]
