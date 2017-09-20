# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombres', models.CharField(max_length=30)),
                ('correos', models.CharField(max_length=40)),
                ('opiniones', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombres', models.CharField(max_length=30)),
                ('correos', models.CharField(max_length=40)),
                ('opiniones', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField(max_length=10)),
            ],
        ),
    ]
