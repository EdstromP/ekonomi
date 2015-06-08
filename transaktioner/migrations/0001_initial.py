# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('namn', models.CharField(max_length=30)),
                ('kommentar', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sokord',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('sokord', models.CharField(max_length=20)),
                ('kategori', models.ForeignKey(to='transaktioner.Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Transaktion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('reskontradatum', models.DateField()),
                ('transaktionsdatum', models.DateField()),
                ('text', models.CharField(max_length=50)),
                ('belopp', models.FloatField()),
                ('kommentar', models.TextField(max_length=500)),
                ('kategori', models.ForeignKey(to='transaktioner.Kategori')),
            ],
        ),
    ]
