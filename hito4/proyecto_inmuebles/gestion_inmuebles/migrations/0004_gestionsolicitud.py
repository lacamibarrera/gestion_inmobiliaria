# Generated by Django 5.1.1 on 2024-12-09 14:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0003_solicitud'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GestionSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('No disponible', 'No disponible'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=20)),
                ('arrendatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gestion_solicitudes', to=settings.AUTH_USER_MODEL)),
                ('id_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud', to='gestion_inmuebles.solicitud')),
                ('inmueble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_gestion', to='gestion_inmuebles.inmueble')),
            ],
        ),
    ]
