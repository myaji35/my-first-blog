# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-09 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_code', models.CharField(max_length=10, unique=True, verbose_name='종목코드')),
                ('company_nm', models.CharField(max_length=50, verbose_name='회사명')),
                ('st_market', models.CharField(max_length=10, verbose_name='종목시장')),
            ],
        ),
    ]
