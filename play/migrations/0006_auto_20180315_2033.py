# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-15 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0005_auto_20180315_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='team_logos/'),
        ),
    ]