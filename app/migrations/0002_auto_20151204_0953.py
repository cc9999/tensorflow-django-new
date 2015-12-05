# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tensormodel',
            name='label',
            field=models.TextField(choices=[('[0,0,0,0,0,0,0,0,0,0]', '0'), ('[0,1,0,0,0,0,0,0,0,0]', '1'), ('[0,0,1,0,0,0,0,0,0,0]', '2'), ('[0,0,0,1,0,0,0,0,0,0]', '3'), ('[0,0,0,0,1,0,0,0,0,0]', '4'), ('[0,0,0,0,0,1,0,0,0,0]', '5'), ('[0,0,0,0,0,0,1,0,0,0]', '6'), ('[0,0,0,0,0,0,0,1,0,0]', '7'), ('[0,0,0,0,0,0,0,0,1,0]', '8'), ('[0,0,0,0,0,0,0,0,0,1]', '9')]),
        ),
    ]
