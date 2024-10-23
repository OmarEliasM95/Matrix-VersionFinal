# Generated by Django 3.2.25 on 2024-09-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0001_initial'),
        ('Productos', '0034_alter_producto_proveedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='proveedores',
            field=models.ManyToManyField(through='Productos.Producto_Intermedia', to='Proveedores.Proveedor'),
        ),
    ]
