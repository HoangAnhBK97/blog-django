# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('image', models.FileField(null=True, upload_to=b'')),
            ],
        ),
    ]
