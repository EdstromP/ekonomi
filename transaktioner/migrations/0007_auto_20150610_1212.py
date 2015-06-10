# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaktioner', '0006_auto_20150610_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Underkategori',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('namn', models.CharField(max_length=30)),
                ('kommentar', models.TextField(blank=True, max_length=500)),
                ('kategori', models.ForeignKey(to='transaktioner.Kategori')),
            ],
        ),
        migrations.AddField(
            model_name='sokord',
            name='underkategori',
            field=models.ForeignKey(null=True, to='transaktioner.Underkategori'),
        ),
    ]
