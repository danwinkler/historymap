# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0008_auto_20151028_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
