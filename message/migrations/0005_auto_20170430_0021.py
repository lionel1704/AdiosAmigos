# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 18:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20170426_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bubye',
            name='alumini',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
