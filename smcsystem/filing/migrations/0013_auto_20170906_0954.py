# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-06 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filing', '0012_cq_group_www'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cq_code',
            name='start',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='启动方法'),
        ),
    ]
