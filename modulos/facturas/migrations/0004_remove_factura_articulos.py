# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0003_auto_20160828_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='articulos',
        ),
    ]
