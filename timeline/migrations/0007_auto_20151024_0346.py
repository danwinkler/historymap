# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0006_auto_20151024_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='latlong',
        ),
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(default=0, blank=True),
            preserve_default=False,
        ),
    ]
