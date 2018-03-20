# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0012_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.URLField()),
                ('image', models.CharField(default='N/A', max_length=250)),
                ('publication_date', models.DateTimeField()),
            ],
        ),
    ]
