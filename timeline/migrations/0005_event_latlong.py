# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='latlong',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
