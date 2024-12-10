from django.contrib import admin
from django.urls import path
from gestion_inmuebles import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'), name ='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('crear_solicitud/<int:inmueble_id>/', views.crear_solicitud, name='crear_solicitud'),
    path('detalle_solicitud/<int:solicitud_id>/', views.detalle_solicitud, name='detalle_solicitud'),
    path('listar_inmuebles/', views.listar_inmuebles, name = 'listar_inmuebles'),
    path('agregar_inmueble/', views.agregar_inmueble, name='agregar_inmueble'),
    path('get_comunas/<int:region_id>/', views.get_comunas, name='get_comunas'),
    path('detalle_inmueble/<int:inmueble_id>/', views.detalle_inmueble, name='detalle_inmueble'),
    path('editar_inmueble/<int:inmueble_id>/', views.editar_inmueble, name='editar_inmueble'),
    path('listar_solicitudes_arrendador/', views.listar_solicitudes_arrendador, name='listar_solicitudes_arrendador'),
    path('listar_solicitudes_arrendatario/', views.listar_solicitudes_arrendatario, name='listar_solicitudes_arrendatario'),
    path('gestionar-solicitud/<int:solicitud_id>/', views.gestionar_solicitud, name='gestionar_solicitud'),
    path('solicitud_success/', views.solicitud_success, name= 'solicitud_success'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)