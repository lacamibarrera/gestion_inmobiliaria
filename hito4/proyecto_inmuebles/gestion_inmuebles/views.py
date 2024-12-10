from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile ,Inmueble, Region, Comuna,Solicitud, GestionSolicitud
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm, EditarPerfilForm, InmuebleForm, SolicitudForm
from django.http import JsonResponse

#Usuarios
def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirigir a la página de login
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

@login_required
def editar_perfil(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('home') 
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = EditarPerfilForm(instance=user_profile, initial={
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        })
    return render(request, 'editar_perfil.html', {'form': form})
# Crear una Región
def crear_region(request):
    if request.method == "POST":
        nombre_region = request.POST.get("nombre_region")
        Region.objects.create(nombre_region=nombre_region)
        return HttpResponse("Región creada exitosamente")
    return render(request, 'crear_region.html')

# Listar todas las Regiones
def listar_regiones(request):
    regiones = Region.objects.all()
    return render(request, 'listar_regiones.html', {'regiones': regiones})

# Actualizar una Región
def actualizar_region(request, id_region):
    region = get_object_or_404(Region, id_region=id_region)
    
    if request.method == "POST":
        region.nombre_region = request.POST.get("nombre_region")
        region.save()
        return HttpResponse("Región actualizada exitosamente")
    
    return render(request, 'actualizar_region.html', {'region': region})

# Borrar una Región
def borrar_region(request, id_region):
    region = get_object_or_404(Region, id_region=id_region)
    region.delete()
    return HttpResponse("Región eliminada exitosamente")

#comuna
def crear_comuna(request):
    if request.method == "POST":
        nombre_comuna = request.POST.get("nombre_comuna")
        region_id = request.POST.get("id_region")
        region = get_object_or_404(Region, pk=region_id)
        Comuna.objects.create(nombre_comuna=nombre_comuna, id_region=region)
        return HttpResponse("Comuna creada exitosamente")
    
    regiones = Region.objects.all()
    return render(request, 'crear_comuna.html', {'regiones': regiones})

def listar_comunas(request):
    comunas = Comuna.objects.all()
    return render(request, 'listar_comunas.html', {'comunas': comunas})

def actualizar_comuna(request, id_comuna):
    comuna = get_object_or_404(Comuna, id_comuna=id_comuna)
    
    if request.method == "POST":
        comuna.nombre_comuna = request.POST.get("nombre_comuna")
        region_id = request.POST.get("id_region")
        comuna.id_region = get_object_or_404(Region, pk=region_id)
        comuna.save()
        return HttpResponse("Comuna actualizada exitosamente")
    
    regiones = Region.objects.all()
    return render(request, 'actualizar_comuna.html', {'comuna': comuna, 'regiones': regiones})

def borrar_comuna(request, id_comuna):
    comuna = get_object_or_404(Comuna, id_comuna=id_comuna)
    comuna.delete()
    return HttpResponse("Comuna eliminada exitosamente")


#Inmueble
@login_required
def agregar_inmueble(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.tipo != 'ARRENDADOR':
        messages.error(request, "Solo los usuarios de tipo 'Arrendador' pueden agregar inmuebles.")
        return redirect('home')  

    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.usuario = request.user
            inmueble.save()
            messages.success(request, "Inmueble agregado con éxito.")
            return redirect('listar_inmuebles')  
    else:
        form = InmuebleForm()
    
    return render(request, 'agregar_inmueble.html', {'form': form})


@login_required
def listar_inmuebles(request):
    # Obtén los filtros de región y comuna si existen en los parámetros de la solicitud
    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')
    
    # Obtén el perfil del usuario
    user_profile = UserProfile.objects.get(user=request.user)

    # Filtra los inmuebles por el usuario en sesión dependiendo del tipo de usuario
    if user_profile.tipo == 'ARRENDADOR':
        inmuebles = Inmueble.objects.select_related('id_comuna__id_region', 'id_region').filter(usuario=request.user)
    else:
        # Para el arrendatario, puedes mostrar todos los inmuebles disponibles
        inmuebles = Inmueble.objects.select_related('id_comuna__id_region', 'id_region').filter(estado='Disponible')  # Suponiendo que 'estado' es el campo que indica si está disponible
    
    # Aplica los filtros adicionales de región y comuna si están presentes
    if region_id:
        inmuebles = inmuebles.filter(id_region_id=region_id)
    if comuna_id:
        inmuebles = inmuebles.filter(id_comuna_id=comuna_id)

    # Debug: Verifica que los datos de comuna y región están siendo obtenidos
    for inmueble in inmuebles:
        print(f"Comuna: {inmueble.id_comuna.nombre_comuna}, Región: {inmueble.id_region.nombre_region}, Estado: {inmueble.estado}")

    # Obtén todas las regiones y comunas para los filtros
    regiones = Region.objects.all()
    comunas = Comuna.objects.filter(id_region_id=region_id) if region_id else Comuna.objects.none()
    
    # Renderiza el template con los datos
    return render(request, 'listar_inmuebles.html', {
        'inmuebles': inmuebles,
        'regiones': regiones,
        'comunas': comunas,
        'selected_region': region_id,
        'selected_comuna': comuna_id
    })

@login_required
def editar_inmueble(request, inmueble_id):
    # Obtener el inmueble a editar o devolver 404 si no existe
    inmueble = get_object_or_404(Inmueble, id_inmueble=inmueble_id)

    # Verificar que el usuario sea el propietario del inmueble y que sea "Arrendador"
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.tipo != 'ARRENDADOR' or inmueble.usuario != request.user:
        messages.error(request, "No tienes permisos para editar este inmueble.")
        return redirect('listar_inmuebles')  # Redirige a la lista de inmuebles o a otra página

    if request.method == 'POST':
        # Si la solicitud es para eliminar el inmueble
        if 'eliminar_inmueble' in request.POST:
            inmueble.delete()
            messages.success(request, "Inmueble eliminado con éxito.")
            return redirect('listar_inmuebles')  # Redirige a la lista de inmuebles después de eliminar

        # Si la solicitud es para actualizar el inmueble
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            messages.success(request, "Inmueble actualizado con éxito.")
            return redirect('listar_inmuebles')  # Redirige a la lista de inmuebles después de actualizar
    else:
        form = InmuebleForm(instance=inmueble)

    return render(request, 'editar_inmueble.html', {'form': form, 'inmueble': inmueble})


def detalle_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id_inmueble=inmueble_id)
    return render(request, 'detalle_inmueble.html', {'inmueble': inmueble})

#Hito2configuracion de la autenticacion
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')



@login_required
def logout_view(request):
    logout(request) 
    return render(request, 'logout_success.html')

@login_required
def crear_solicitud(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id_inmueble=inmueble_id)

    if inmueble.usuario == request.user:  # Cambiado request.usuario a request.user
        messages.error(request, "No puedes solicitar tu propio inmueble.")
        return redirect('home')

    if inmueble.estado == "NO_DISPONIBLE":
        messages.error(request, "Este inmueble no está disponible para solicitar.")
        return redirect('detalle_inmueble', inmueble_id=inmueble.id_inmueble)

    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            mensaje = form.cleaned_data['mensaje']
           
            solicitud = Solicitud.objects.create(
                arrendador=request.user,  # Cambiado request.usuario a request.user
                arrendatario=inmueble.usuario,
                inmueble=inmueble,
                mensaje=mensaje
            )
            messages.success(request, "Solicitud creada exitosamente.")
            return redirect('solicitud_success')
    else:
        form = SolicitudForm()

    return render(request, 'crear_solicitud.html', {'form': form, 'inmueble': inmueble})

@login_required
def solicitud_success(request): 
    return render(request, 'solicitud_success.html')

def detalle_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    return render(request, 'detalle_solicitud.html', {'solicitud': solicitud})

@login_required
def listar_solicitudes_arrendador(request):
    
    solicitudes = Solicitud.objects.filter(arrendador=request.user)
    return render(request, 'listar_solicitudes_arrendador.html', {'solicitudes': solicitudes})

@login_required
def listar_solicitudes_arrendatario(request):
  
    solicitudes = Solicitud.objects.filter(arrendatario=request.user)
    return render(request, 'listar_solicitudes_arrendatario.html', {'solicitudes': solicitudes})

@login_required
def gestionar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id, arrendatario=request.user)

    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in ['Pendiente', 'Aceptada', 'Rechazada']:
            solicitud.estado = nuevo_estado
            solicitud.save()
            messages.success(request, "Estado de la solicitud actualizado correctamente.")
        else:
            messages.error(request, "Estado inválido.")
        return redirect('listar_solicitudes_arrendatario')
    return redirect('home')

def home(request):

    inmuebles = Inmueble.objects.all()  # Asegúrate de que hay inmuebles en la base de datos
    for inmueble in inmuebles:
        print(f"Inmueble ID: {inmueble.id_inmueble}, Nombre: {inmueble.nombre}")

    return render(request, 'home.html', {'inmuebles': inmuebles})

def get_comunas(request, region_id):
    # Filtrar las comunas por región
    comunas = Comuna.objects.filter(id_region_id=region_id).values('id_comuna', 'nombre_comuna')
    
    # Devolver las comunas en formato JSON
    return JsonResponse({'comunas': list(comunas)})


@login_required
def gestionar_solicitudes(request):
    # Obtener todas las solicitudes pendientes
    solicitudes = GestionSolicitud.objects.filter(estado='Pendiente')
    return render(request, 'gestionar_solicitudes.html', {'solicitudes': solicitudes})

@login_required
def cambiar_estado_solicitud(request, solicitud_id, accion):
    solicitud = get_object_or_404(GestionSolicitud, id=solicitud_id)
    
    if not request.user.groups.filter(name='Arrendatarios').exists():
        return redirect('error')  # 
    
    if accion == 'aceptar':

        solicitud.estado = 'Aceptada'
        solicitud.save()
        

        inmueble = solicitud.inmueble
        inmueble.estado = 'No disponible'
        inmueble.save()
    
    elif accion == 'rechazar':
  
        solicitud.estado = 'Rechazada'
        solicitud.save()
    
    return redirect('gestionar_solicitudes') 