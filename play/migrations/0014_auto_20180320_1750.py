# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0013_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(null=True),
        ),
    ]
