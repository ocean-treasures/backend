# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
