# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20170705_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progress',
            old_name='max',
            new_name='max_progress',
        ),
    ]
