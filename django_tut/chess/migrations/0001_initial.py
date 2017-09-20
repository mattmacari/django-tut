# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('piece_id', models.AutoField(primary_key=True, serialize=False)),
                ('piece_name', models.CharField(max_length=100)),
            ],
            options={
                'managed': True,
            },
        ),
    ]