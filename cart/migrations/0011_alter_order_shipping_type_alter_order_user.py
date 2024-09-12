# Generated by Django 5.0.7 on 2024-08-25 10:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_alter_orderitem_color_alter_orderitem_size'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_type',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='نوع ارسال'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
