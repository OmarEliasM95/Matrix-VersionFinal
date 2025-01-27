# Generated by Django 3.2.25 on 2024-10-01 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Caja', '0008_caja_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='saldo_final',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='caja',
            name='saldo_inicial',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dinero',
            name='tipo_dinero',
            field=models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], default='', max_length=25, verbose_name='Tipo de movimiento'),
        ),
    ]
