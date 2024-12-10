from django.contrib.auth.models import Group, Permission

def configurar_permisos():
    # Crear grupo "Arrendadores"
    arrendadores_group, created = Group.objects.get_or_create(name='Arrendadores')
    if created:
        print("Grupo 'Arrendadores' creado.")
    permisos_arrendadores = Permission.objects.filter(codename__in=['add_inmueble', 'change_inmueble'])
    arrendadores_group.permissions.add(*permisos_arrendadores)

    # Crear grupo "Arrendatarios"
    arrendatarios_group, created = Group.objects.get_or_create(name='Arrendatarios')
    if created:
        print("Grupo 'Arrendatarios' creado.")
    permiso_contactar = Permission.objects.get(codename='contact_inmueble')
    arrendatarios_group.permissions.add(permiso_contactar)

    # Crear grupo "Administradores"
    administradores_group, created = Group.objects.get_or_create(name='Administradores')
    if created:
        print("Grupo 'Administradores' creado.")
    permisos_administradores = Permission.objects.filter(codename__in=['add_user', 'change_user', 'add_inmueble', 'change_inmueble'])
    administradores_group.permissions.add(*permisos_administradores)

    print("Grupos y permisos configurados correctamente.")