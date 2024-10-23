# Generated by Django 3.2.25 on 2024-09-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0002_alter_proveedor_provincia'),
        ('Productos', '0055_alter_producto_proveedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='proveedores',
            field=models.ManyToManyField(through='Productos.Producto_Intermedia', to='Proveedores.Proveedor'),
        ),
    ]
