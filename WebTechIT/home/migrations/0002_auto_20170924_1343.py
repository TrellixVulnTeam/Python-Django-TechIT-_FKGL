# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Photographer',
        ),
        migrations.RemoveField(
            model_name='tintuc',
            name='Creator',
        ),
        migrations.RemoveField(
            model_name='tintuc',
            name='Id_DanhMuc',
        ),
        migrations.RemoveField(
            model_name='tintuc',
            name='Id_LoaiTin',
        ),
        migrations.RemoveField(
            model_name='tintuc',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tthagtag',
            name='Id_HashTag',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='HashTag',
        ),
        migrations.DeleteModel(
            name='TinTuc',
        ),
        migrations.DeleteModel(
            name='TTHagTag',
        ),
    ]