# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_progress_pictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3)),
                ('rope_lenght', models.IntegerField()),
                ('pictures', models.ManyToManyField(to='game.Picture')),
            ],
        ),
    ]
