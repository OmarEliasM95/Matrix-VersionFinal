# Generated by Django 5.0.7 on 2024-08-25 16:54

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Productos', '__first__'),
        ('Proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField(default=datetime.datetime.now)),
                ('total', models.IntegerField()),
                ('metodo_pago', models.CharField(choices=[('', ''), ('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'), ('Tarjeta_de_Debito', 'Tarjeta de Debito'), ('Tarjeta_de_Credito', 'Tarjeta de Credito')], default='', max_length=25)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Proveedores.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Compra_intermedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_de_compra', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Compras.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='productos',
            field=models.ManyToManyField(through='Compras.Compra_intermedio', to='Productos.producto'),
        ),
    ]