# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-10 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_mobile_api'),
    ]

    operations = [
        migrations.CreateModel(
            name='API_VERSION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_version', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'api\u7248\u672c\u53f7',
                'verbose_name_plural': 'api\u7248\u672c\u53f7',
            },
        ),
    ]
