# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_auto_20160326_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='added',
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
