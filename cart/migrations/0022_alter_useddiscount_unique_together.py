# Generated by Django 5.0.7 on 2024-08-27 19:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0021_alter_useddiscount_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useddiscount',
            unique_together={('user', 'discount')},
        ),
    ]
