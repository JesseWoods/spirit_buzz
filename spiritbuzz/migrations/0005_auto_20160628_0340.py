# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 03:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spiritbuzz', '0004_auto_20160628_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchterm',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='SearchTerm',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
