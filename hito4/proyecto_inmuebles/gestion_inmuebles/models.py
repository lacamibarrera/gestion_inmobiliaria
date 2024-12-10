from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('ARRENDATARIO', 'Arrendatario'),
        ('ARRENDADOR', 'Arrendador'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    tipo = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default="Arrendador")
    rut = models.CharField(max_length= 12)
    direccion = models.CharField(max_length= 300)
    telefono = models.CharField(max_length= 12)
    fecha_registro = models.DateTimeField(auto_now_add=True)
 
class Region(models.Model):
    id_region = models.AutoField(primary_key= True)
    nombre_region = models.CharField(max_length= 300)

    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    id_comuna= models.AutoField(primary_key= True)
    nombre_comuna = models.CharField(max_length= 250)
    id_region = models.ForeignKey('Region',on_delete=models.CASCADE )
    
    def __str__(self):
        return self.nombre_comuna

class TipoInmueble(models.Model): 
    id_tipo_inmueble = models.AutoField(primary_key= True)
    tipo_inmueble = models.CharField(max_length= 100)

class Inmueble(models.Model): 

    ESTADO_CHOICES = (
        ('DISPONIBLE', 'Disponible'),
        ('NO_DISPONIBLE', 'No_Disponible'),
    )
    TIPO_CHOICES = (
        ('CASA', 'Casa'),
        ('DEPARTAMENTO', 'Departamento'),
        ('CABAÑA', 'Cabaña'),
        ('OFICINA', 'Oficina'),
        ('BODEGA', 'Bodega'),
        ('OTRO', 'Otro'),
    )
    id_inmueble = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_terreno = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length= 300)
    id_comuna = models.ForeignKey('Comuna', on_delete= models.CASCADE)
    id_region = models.ForeignKey('Region', on_delete= models.CASCADE)
    precio_mensual = models.DecimalField(max_digits= 12, decimal_places= 2)
    tipo_inmueble = models.TextField(max_length= 20, choices= TIPO_CHOICES, default="Otro")
    imagen_url = models.URLField(max_length=300, null=True, blank=True) 
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="Disponible")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inmuebles',default='1')
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    ultima_modificacion = models.DateTimeField(auto_now=True)


class Solicitud(models.Model):
    arrendador = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="solicitudes_creadas"
    ) 
    arrendatario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="mis_solicitudes"
        
    ) # Usuario que hace la solicitud
    inmueble = models.ForeignKey(
        Inmueble, 
        on_delete=models.CASCADE, 
        related_name="solicitudes"
    )  # Inmueble sobre el que se hace la solicitud
    mensaje = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=[
            ('Pendiente', 'Pendiente'),
            ('Aceptada', 'Aceptada'),
            ('Rechazada', 'Rechazada')
        ],
        default='Pendiente'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.arrendador.username} para {self.inmueble.nombre}, de {self.arrendatario.username}"
    
class GestionSolicitud(models.Model):
    arrendatario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="gestion_solicitudes"
    )  # Usuario que hace la solicitud
    inmueble = models.ForeignKey(
        Inmueble, 
        on_delete=models.CASCADE, 
        related_name="solicitudes_gestion"
    )
    nombre = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('Disponible', 'Disponible'),
            ('No disponible', 'No disponible'),
            ('Pendiente','Pendiente')
        ],
        default='Pendiente'
    )
    id_solicitud = models.ForeignKey(Solicitud, related_name='solicitud', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
