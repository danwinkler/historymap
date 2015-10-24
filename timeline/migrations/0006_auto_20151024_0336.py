# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_event_latlong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='latlong',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.TextField(blank=True),
        ),
    ]
