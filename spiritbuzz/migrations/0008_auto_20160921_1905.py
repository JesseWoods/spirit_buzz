# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-21 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiritbuzz', '0007_auto_20160629_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(upload_to='images/products/thumbnails'),
        ),
    ]
