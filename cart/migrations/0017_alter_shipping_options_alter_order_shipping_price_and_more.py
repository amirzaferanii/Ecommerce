# Generated by Django 5.0.7 on 2024-08-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shipping',
            options={'verbose_name': 'حمل و نقل', 'verbose_name_plural': 'حمل و نقل ها'},
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_price',
            field=models.IntegerField(default=0, verbose_name='هزینه ارسال'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='color',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='سایز'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total',
            field=models.PositiveIntegerField(default=0, verbose_name='جمع'),
        ),
    ]
