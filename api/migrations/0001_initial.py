# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-09 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MOBILE_API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=100, null=True)),
                ('api_version', models.IntegerField(max_length=100, null=True)),
                ('api_device', models.IntegerField(choices=[(0, '\u82f9\u679c'), (1, '\u5b89\u5353'), (2, '\u5176\u4ed6')], max_length=100)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u79fb\u52a8\u7aefAPI',
                'verbose_name_plural': '\u79fb\u52a8\u7aefAPI',
            },
        ),
    ]