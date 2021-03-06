# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studapp', '0002_auto_20170513_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(blank=True, max_length=6)),
                ('session', models.CharField(blank=True, max_length=20)),
                ('type_exam', models.CharField(blank=True, max_length=10)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
