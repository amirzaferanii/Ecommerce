# Generated by Django 5.0.7 on 2024-08-18 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='موجودی')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.color', verbose_name='رنگ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='product.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.size', verbose_name='سایز')),
            ],
            options={
                'verbose_name': 'موجودی',
                'verbose_name_plural': 'موجودی محصولات',
                'unique_together': {('product', 'size', 'color')},
            },
        ),
    ]