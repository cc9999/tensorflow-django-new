# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151204_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tensormodel',
            name='label',
            field=models.CharField(choices=[('[0,0,0,0,0,0,0,0,0,0]', '0'), ('[0,1,0,0,0,0,0,0,0,0]', '1'), ('[0,0,1,0,0,0,0,0,0,0]', '2'), ('[0,0,0,1,0,0,0,0,0,0]', '3'), ('[0,0,0,0,1,0,0,0,0,0]', '4'), ('[0,0,0,0,0,1,0,0,0,0]', '5'), ('[0,0,0,0,0,0,1,0,0,0]', '6'), ('[0,0,0,0,0,0,0,1,0,0]', '7'), ('[0,0,0,0,0,0,0,0,1,0]', '8'), ('[0,0,0,0,0,0,0,0,0,1]', '9')], default=None, max_length=50),
        ),
    ]
