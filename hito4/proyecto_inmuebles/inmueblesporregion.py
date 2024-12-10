import django
import os

# Establecer el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings') 
django.setup()

from gestion_inmuebles.models import Inmueble, Region

# Consultar inmuebles para arriendo, solo los campos 'nombre', 'descripcion', 'id_region', agrupados por región
inmuebles = Inmueble.objects.filter(estado="Disponible", activo=True).values('nombre', 'descripcion', 'id_region')

# Imprimir la consulta SQL generada por Django
print(inmuebles.query)

# Consultar las regiones que tienen inmuebles disponibles en arriendo
regiones_con_inmuebles = Inmueble.objects.filter(estado="Disponible", activo=True).values('id_region').distinct()


with open("inmuebles_arriendo_por_region.txt", "w", encoding="utf-8") as f:
    # Recorrer las regiones que tienen inmuebles disponibles
    for region_data in regiones_con_inmuebles:
        region = Region.objects.get(id_region=region_data['id_region'])

        # Filtrar los inmuebles de esa región
        inmuebles_region = inmuebles.filter(id_region=region.id_region)

        # Escribir el nombre de la región como encabezado
        f.write(f"Región: {region.nombre_region}\n")
        f.write("=" * 40 + "\n")
        
        # Escribir los inmuebles en esa región
        for inmueble in inmuebles_region:
            f.write(f"Nombre: {inmueble['nombre']}\n")
            f.write(f"Descripción: {inmueble['descripcion']}\n")
            f.write("-" * 40 + "\n")
        
        f.write("\n\n")