# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('type', '0002_userimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeimage',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
