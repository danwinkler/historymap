# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_event_end'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end',
            new_name='other',
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(default=b'SI', max_length=2, choices=[(b'SI', b'Single'), (b'SS', b'Span Start'), (b'SE', b'Span End')]),
        ),
    ]
