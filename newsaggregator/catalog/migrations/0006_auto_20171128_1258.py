# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 12:58
from __future__ import unicode_literals

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20171128_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(default=120, help_text='Select a genre for this news', max_length=100, verbose_name=catalog.models.Genre),
            preserve_default=False,
        ),
    ]
