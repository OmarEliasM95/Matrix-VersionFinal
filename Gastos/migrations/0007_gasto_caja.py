# Generated by Django 3.2.25 on 2024-10-01 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Caja', '0007_dinero_caja'),
        ('Gastos', '0006_remove_gasto_tipo_gasto'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='caja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gastos', to='Caja.caja'),
        ),
    ]
