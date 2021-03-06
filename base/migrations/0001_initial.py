# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-07 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sendMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('usermessage', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='uploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('userFile', models.FileField(upload_to='')),
            ],
        ),
    ]
