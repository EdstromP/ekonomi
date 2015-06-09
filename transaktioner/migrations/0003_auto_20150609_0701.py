# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaktioner', '0002_auto_20150608_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaktion',
            name='importdatum',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='transaktion',
            name='kalla',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
