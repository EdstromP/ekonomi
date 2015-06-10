# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaktioner', '0005_auto_20150609_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='namn',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='sokord',
            name='sokord',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
