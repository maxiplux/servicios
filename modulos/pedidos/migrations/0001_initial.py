# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 23:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facturas', '0004_remove_factura_articulos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('direccion', models.CharField(max_length=255)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.Factura')),
                ('mensajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajero', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
