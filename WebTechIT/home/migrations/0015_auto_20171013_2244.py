# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20171009_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tintuc',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]
