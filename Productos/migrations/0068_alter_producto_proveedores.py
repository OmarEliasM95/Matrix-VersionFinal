# Generated by Django 3.2.25 on 2024-10-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0003_alter_proveedor_telefono'),
        ('Productos', '0067_remove_producto_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='proveedores',
            field=models.ManyToManyField(through='Productos.Producto_Intermedia', to='Proveedores.Proveedor'),
        ),
    ]
