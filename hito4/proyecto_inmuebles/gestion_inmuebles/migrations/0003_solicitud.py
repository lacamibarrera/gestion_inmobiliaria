# Generated by Django 5.1.1 on 2024-12-08 23:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0002_remove_inmueble_activo_inmueble_tipo_inmueble_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aceptada', 'Aceptada'), ('Rechazada', 'Rechazada')], default='Pendiente', max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('arrendador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_creadas', to=settings.AUTH_USER_MODEL)),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='gestion_inmuebles.inmueble')),
            ],
        ),
    ]