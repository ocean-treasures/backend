# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20170712_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='pictures',
            field=models.ManyToManyField(to='game.Picture'),
        ),
    ]