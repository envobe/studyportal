# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-30 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import functools
import studapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0016_auto_20170530_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=functools.partial(studapp.models._update_filename, *(), **{b'path': 'documents/'})),
        ),
    ]
