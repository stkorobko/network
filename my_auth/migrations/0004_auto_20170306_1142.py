# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0003_auto_20170303_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
