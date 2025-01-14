# Generated by Django 5.0.7 on 2024-08-27 19:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0020_useddiscount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useddiscount',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='useddiscount',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.discountcode', verbose_name='کد تخفیف'),
        ),
        migrations.AlterField(
            model_name='useddiscount',
            name='used_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='استفاده شده'),
        ),
        migrations.AlterField(
            model_name='useddiscount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
