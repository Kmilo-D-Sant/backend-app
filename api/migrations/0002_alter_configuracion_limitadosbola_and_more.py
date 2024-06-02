# Generated by Django 4.0.6 on 2024-03-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosBola',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosBolaBote',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosBolaBoteUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosBolaUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosCentena',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosCentenaBote',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosCentenaBoteUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosCentenaUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosParlet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosParletBote',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosParletBoteUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='limitadosParletUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaBola',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaBolaBote',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaBolaBoteUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaBolaUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaCentena',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaCentenaBote',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaCentenaBoteUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaCentenaUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaParlet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaParletBote',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaParletBoteUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='noSeJuegaParletUsuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
