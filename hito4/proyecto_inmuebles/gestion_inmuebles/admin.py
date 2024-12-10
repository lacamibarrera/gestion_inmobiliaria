from django.contrib import admin
from django.utils import timezone
from .models import Inmueble, Region, Comuna, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0  # No crear instancias vacías adicionales

class CustomUserAdmin(UserAdmin):
    # Agregar el inline de UserProfile
    inlines = [UserProfileInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion','precio_mensual')
    search_fields = ('nombre', 'direccion')
    list_filter = ('precio_mensual', 'id_region')
    readonly_fields = ('fecha_creacion', 'ultima_modificacion')
    
    def save_model(self, request, obj, form, change):
        if change: 
          obj.ultima_modificacion = timezone.now()
        else:
          obj.fecha_creacion = timezone.now()
        obj.save()
        
@admin.register(Region)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('id_region', 'nombre_region',)
    search_fields = ('id_region','nombre_region')
    list_filter = ('nombre_region', 'id_region')

@admin.register(Comuna)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('id_comuna', 'nombre_comuna', 'id_region')
    search_fields = ('id_comuna', 'nombre_comuna')
    list_filter = ('nombre_comuna', 'id_region')