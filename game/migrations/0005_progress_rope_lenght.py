# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20170707_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='rope_lenght',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
    ]
