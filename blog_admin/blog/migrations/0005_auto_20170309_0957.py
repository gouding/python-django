# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='id',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
