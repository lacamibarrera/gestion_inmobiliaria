import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

from gestion_inmuebles.models import Inmueble, Comuna

# Consultar inmuebles para arriendo, solo los campos 'nombre' y 'descripcion', agrupados por comuna
inmuebles = Inmueble.objects.filter(estado="Disponible", activo=True).values('nombre', 'descripcion', 'id_comuna')

# Mostrar la consulta SQL generada por Django
print(inmuebles.query)

# Consultar comunas para obtener su nombre
comunas = Comuna.objects.all()

# Crear un archivo de texto donde se almacenarán los resultados en UTF-8
with open("inmuebles_arriendo_por_comuna.txt", "w", encoding="utf-8") as f:
    # Recorrer las comunas
    for comuna in comunas:
        # Filtrar los inmuebles de esa comuna
        inmuebles_comuna = inmuebles.filter(id_comuna=comuna.id_comuna)

        # Si hay inmuebles disponibles en esta comuna, escribir en el archivo
        if inmuebles_comuna.exists():
            # Escribir el nombre de la comuna como encabezado
            f.write(f"Comuna: {comuna.nombre_comuna}\n")
            f.write("=" * 40 + "\n")
            
            # Escribir los inmuebles en esa comuna
            for inmueble in inmuebles_comuna:
                f.write(f"Nombre: {inmueble['nombre']}\n")
                f.write(f"Descripción: {inmueble['descripcion']}\n")
                f.write("-" * 40 + "\n")
            
            f.write("\n\n")