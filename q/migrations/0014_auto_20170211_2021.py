# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import q.models


class Migration(migrations.Migration):

    dependencies = [
        ('q', '0013_auto_20170211_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to=q.models.Comments.comments_path, verbose_name='Добавить изображение'),
        ),
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to=q.models.Post.post_path, verbose_name='Добавить изображение'),
        ),
    ]
