# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-16 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0008_auto_20180316_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='thumbnail',
            field=models.CharField(default='N/A', max_length=250),
        ),
    ]
