# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_auto_20160828_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefactura',
            name='articulo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.Producto'),
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturas.Factura'),
        ),
    ]