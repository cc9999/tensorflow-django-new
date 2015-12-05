# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151204_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tensormodel',
            name='label',
            field=models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], max_length=50, default=None),
        ),
    ]
