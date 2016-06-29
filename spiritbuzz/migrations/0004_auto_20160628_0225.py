# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiritbuzz', '0003_auto_20160627_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='picture',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images', upload_to='images/products/main'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_caption',
            field=models.CharField(default='Product Image', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default='images', upload_to='images/products/thumbnails'),
        ),
    ]
