# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 19:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_picture_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='rope_lenght',
        ),
    ]