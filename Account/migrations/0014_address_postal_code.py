# Generated by Django 5.0.7 on 2024-08-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0013_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='postal_code',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]