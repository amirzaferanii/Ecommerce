# Generated by Django 5.0.7 on 2024-09-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0019_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='نام کامل'),
        ),
    ]
