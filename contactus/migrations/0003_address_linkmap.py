# Generated by Django 5.0.7 on 2024-08-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0002_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='linkmap',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
