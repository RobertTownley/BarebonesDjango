# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeltest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='can_add_fields',
            field=models.BooleanField(default=True),
        ),
    ]
