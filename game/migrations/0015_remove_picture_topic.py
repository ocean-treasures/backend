# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 11:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_picture_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='topic',
        ),
    ]
