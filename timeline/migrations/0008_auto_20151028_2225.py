# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0007_auto_20151024_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='month',
            field=models.IntegerField(default=1),
        ),
    ]
