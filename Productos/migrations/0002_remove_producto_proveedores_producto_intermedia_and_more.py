# Generated by Django 5.0.7 on 2024-08-27 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
        ('Proveedores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='proveedores',
        ),
        migrations.CreateModel(
            name='producto_intermedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proveedores.proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedores',
            field=models.ManyToManyField(through='Productos.producto_intermedia', to='Proveedores.proveedor'),
        ),
    ]