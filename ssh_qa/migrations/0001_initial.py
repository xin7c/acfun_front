# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-01 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frontdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]