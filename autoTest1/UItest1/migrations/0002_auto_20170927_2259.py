# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-27 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UItest1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='key_words',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='step',
            name='locate_content',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AddField(
            model_name='step',
            name='locate_way',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='step',
            name='sp_assert',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='step',
            name='value',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
    ]
