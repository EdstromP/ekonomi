# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaktioner', '0003_auto_20150609_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaktion',
            name='radnr',
            field=models.IntegerField(null=True),
        ),
    ]
