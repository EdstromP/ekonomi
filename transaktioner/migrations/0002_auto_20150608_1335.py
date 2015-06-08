# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaktioner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='kommentar',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='transaktion',
            name='kategori',
            field=models.ForeignKey(null=True, to='transaktioner.Kategori'),
        ),
        migrations.AlterField(
            model_name='transaktion',
            name='kommentar',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
