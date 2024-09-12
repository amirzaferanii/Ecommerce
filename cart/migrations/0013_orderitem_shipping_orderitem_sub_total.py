# Generated by Django 5.0.7 on 2024-08-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_orderitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='shipping',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='sub_total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]