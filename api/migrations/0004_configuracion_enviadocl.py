# Generated by Django 5.0.3 on 2024-06-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_usuario_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='enviadoCl',
            field=models.BooleanField(default=False),
        ),
    ]
