# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 06:45
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20170924_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Create_date', models.DateTimeField(auto_now_add=True)),
                ('Update_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Is_Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Create_date', models.DateTimeField(auto_now_add=True)),
                ('Update_date', models.DateTimeField(auto_now=True)),
                ('Name', models.CharField(max_length=255)),
                ('Image', models.FileField(null=True, upload_to='images')),
                ('alt', models.CharField(max_length=50, null=True)),
                ('Is_Allowlink', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Is_Display', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TinTuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Create_date', models.DateTimeField(auto_now_add=True)),
                ('Update_date', models.DateTimeField(auto_now=True)),
                ('Title', models.CharField(max_length=255)),
                ('Decriptions', models.CharField(max_length=255, null=True)),
                ('Content', ckeditor.fields.RichTextField(null=True, verbose_name='Noi dung')),
                ('Image', models.FileField(null=True, upload_to='images')),
                ('Views', models.IntegerField(default=0)),
                ('Is_HightLight', models.BooleanField(default=False)),
                ('Creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Id_DanhMuc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.DanhMuc')),
                ('Id_LoaiTin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.LoaiTin')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TTHagTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Is_Status', models.BooleanField(default=True)),
                ('Id_HashTag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.HashTag')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.TinTuc'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
