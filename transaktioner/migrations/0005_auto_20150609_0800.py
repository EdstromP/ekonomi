# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaktioner', '0004_transaktion_radnr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaktion',
            name='reskontradatum',
            field=models.DateField(null=True),
        ),
    ]
