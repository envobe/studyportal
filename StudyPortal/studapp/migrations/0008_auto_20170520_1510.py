# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0007_document_typ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='typ',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='studapp.Minor1'),
        ),
    ]
