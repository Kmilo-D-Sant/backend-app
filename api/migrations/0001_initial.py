# Generated by Django 4.0.6 on 2024-03-23 13:31

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('fecha', models.BigIntegerField(default=0)),
                ('horaAperturaDia', models.CharField(default='06:00:00', max_length=20)),
                ('horaCierreDia', models.CharField(default='13:15:00', max_length=20)),
                ('horaAperturaNoche', models.CharField(default='14:00:00', max_length=20)),
                ('horaCierreNoche', models.CharField(default='21:20:00', max_length=20)),
                ('beneficioCliente', models.FloatField(default=0.3)),
                ('beneficioClienteBote', models.FloatField(default=0.1)),
                ('beneficioClienteBola', models.FloatField(default=0.2)),
                ('beneficioClienteBolaBote', models.FloatField(default=0.1)),
                ('pagoFijo', models.IntegerField(default=75)),
                ('pagoFijoBote', models.IntegerField(default=80)),
                ('pagoFijoLimitado', models.IntegerField(default=50)),
                ('pagoFijoLimitadoBote', models.IntegerField(default=50)),
                ('pagoCorrido', models.IntegerField(default=25)),
                ('pagoCorridoBote', models.IntegerField(default=20)),
                ('pagoCorridoLimitado', models.IntegerField(default=20)),
                ('pagoCorridoLimitadoBote', models.IntegerField(default=20)),
                ('pagoParlet', models.IntegerField(default=1100)),
                ('pagoParletBote', models.IntegerField(default=1000)),
                ('pagoParletLimitado', models.IntegerField(default=500)),
                ('pagoParletLimitadoBote', models.IntegerField(default=500)),
                ('pagoCentena', models.IntegerField(default=400)),
                ('pagoCentenaLimitado', models.IntegerField(default=200)),
                ('pagoCentenaBote', models.IntegerField(default=400)),
                ('pagoCentenaLimitadoBote', models.IntegerField(default=200)),
                ('topeFijo', models.IntegerField(default=200)),
                ('topeFijoBote', models.IntegerField(default=400)),
                ('topeFijoUsuario', models.IntegerField(default=200)),
                ('topeFijoBoteUsuario', models.IntegerField(default=400)),
                ('topeCorrido', models.IntegerField(default=100)),
                ('topeCorridoBote', models.IntegerField(default=200)),
                ('topeCorridoUsuario', models.IntegerField(default=100)),
                ('topeCorridoBoteUsuario', models.IntegerField(default=200)),
                ('topeCentena', models.IntegerField(default=1000)),
                ('topeCentenaBote', models.IntegerField(default=200)),
                ('topeCentenaUsuario', models.IntegerField(default=100)),
                ('topeCentenaBoteUsuario', models.IntegerField(default=200)),
                ('topeParlet', models.IntegerField(default=10)),
                ('topeParletBote', models.IntegerField(default=20)),
                ('topeParletUsuario', models.IntegerField(default=10)),
                ('topeParletBoteUsuario', models.IntegerField(default=20)),
                ('tiroManana', models.BooleanField(default=True)),
                ('limitadosBola', models.CharField(max_length=100)),
                ('limitadosBolaBote', models.CharField(max_length=100)),
                ('limitadosBolaUsuario', models.CharField(max_length=100)),
                ('limitadosBolaBoteUsuario', models.CharField(max_length=100)),
                ('limitadosParlet', models.CharField(max_length=100)),
                ('limitadosParletUsuario', models.CharField(max_length=100)),
                ('limitadosParletBote', models.CharField(max_length=100)),
                ('limitadosParletBoteUsuario', models.CharField(max_length=100)),
                ('limitadosCentena', models.CharField(max_length=100)),
                ('limitadosCentenaUsuario', models.CharField(max_length=100)),
                ('limitadosCentenaBote', models.CharField(max_length=100)),
                ('limitadosCentenaBoteUsuario', models.CharField(max_length=100)),
                ('noSeJuegaBola', models.CharField(max_length=100)),
                ('noSeJuegaBolaBote', models.CharField(max_length=100)),
                ('noSeJuegaBolaUsuario', models.CharField(max_length=100)),
                ('noSeJuegaBolaBoteUsuario', models.CharField(max_length=100)),
                ('noSeJuegaParlet', models.CharField(max_length=100)),
                ('noSeJuegaParletBote', models.CharField(max_length=100)),
                ('noSeJuegaParletUsuario', models.CharField(max_length=100)),
                ('noSeJuegaParletBoteUsuario', models.CharField(max_length=100)),
                ('noSeJuegaCentena', models.CharField(max_length=100)),
                ('noSeJuegaCentenaBote', models.CharField(max_length=100)),
                ('noSeJuegaCentenaUsuario', models.CharField(max_length=100)),
                ('noSeJuegaCentenaBoteUsuario', models.CharField(max_length=100)),
                ('enviado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Jugada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('usuario', models.CharField(max_length=50, verbose_name='Usuario')),
                ('numeros', models.CharField(max_length=100, verbose_name='Numeros')),
                ('montoFijo', models.FloatField(default=0)),
                ('montoCorrido', models.FloatField(default=0)),
                ('enElBote', models.BooleanField(default=False)),
                ('fecha', models.BigIntegerField(default=0)),
                ('tiroManana', models.BooleanField(default=True)),
                ('premio', models.FloatField(default=0)),
                ('enviado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefono', models.CharField(max_length=10)),
                ('es_proveedor', models.BooleanField(default=False, verbose_name='Es proveedor')),
                ('imagen', models.ImageField(blank=True, default='', null=True, upload_to='imagenes/')),
                ('imagenB64', models.TextField(blank=True, null=True)),
                ('configuracionActualizada', models.BooleanField(default=False, verbose_name='Configuración actual')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
