# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20151225_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.IntegerField(verbose_name='\u0411\u0456\u043b\u0435\u0442'),
        ),
    ]
