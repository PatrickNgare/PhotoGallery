# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='gallery/', width_field='width_field'),
        ),
    ]
