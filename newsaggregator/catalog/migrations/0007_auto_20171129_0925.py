# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20171128_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='news category (e.g. politics, sports etc.)', max_length=200),
        ),
    ]