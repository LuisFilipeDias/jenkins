# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_auto_20160326_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='status',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='job',
            new_name='name',
        ),
    ]
