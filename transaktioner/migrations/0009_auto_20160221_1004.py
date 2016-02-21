# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaktioner', '0008_transaktion_underkategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sokord',
            name='underkategori',
            field=models.ForeignKey(blank=True, null=True, to='transaktioner.Underkategori'),
        ),
        migrations.AlterField(
            model_name='transaktion',
            name='underkategori',
            field=models.ForeignKey(blank=True, null=True, to='transaktioner.Underkategori'),
        ),
    ]
