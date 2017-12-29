# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20171128_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(help_text='hfjhhj', max_length=100),
        ),
    ]
