# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('pictureUrl', models.CharField(max_length=250)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('curr', models.IntegerField()),
                ('max', models.IntegerField()),
            ],
        ),
    ]
