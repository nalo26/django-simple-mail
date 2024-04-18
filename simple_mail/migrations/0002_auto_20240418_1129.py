# Generated by Django 3.2.25 on 2024-04-18 09:29

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_mail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simplemailconfig',
            name='twitter_url',
        ),
        migrations.AddField(
            model_name='simplemailconfig',
            name='x_url',
            field=models.URLField(blank=True, max_length=255, verbose_name='X/Twitter Url'),
        ),
        migrations.AlterField(
            model_name='simplemail',
            name='banner',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='simple_mail', verbose_name='Banner'),
        ),
        migrations.AlterField(
            model_name='simplemailconfig',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to='simple_mail', verbose_name='Logo'),
        ),
    ]
