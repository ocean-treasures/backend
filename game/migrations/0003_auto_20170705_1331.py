# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20170705_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pictureUrl', models.CharField(max_length=250)),
                ('word', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Pictures',
        ),
    ]
