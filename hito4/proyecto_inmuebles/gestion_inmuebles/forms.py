from django import forms
from .models import UserProfile, Inmueble, Solicitud
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    # Campos adicionales del modelo User
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    # Campos adicionales del modelo UserProfile
    tipo = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    rut = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['tipo', 'rut', 'direccion', 'telefono']

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        user_profile = super().save(commit=False)
        user_profile.user = user
        if commit:
            user_profile.save()

        return user_profile

class EditarPerfilForm(forms.ModelForm):
    # Formulario para editar perfil
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(max_length=300, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['tipo', 'direccion', 'telefono']

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre', 'tipo_inmueble', 'descripcion', 'm2_construidos', 'm2_terreno',
            'estacionamientos', 'habitaciones', 'banos', 'direccion', 'id_comuna',
            'id_region', 'precio_mensual', 'estado', 'imagen_url'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
            'precio_mensual': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'imagen_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL de la imagen'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-control'}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2_terreno': forms.NumberInput(attrs={'class': 'form-control'}),
            'estacionamientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'id_region': forms.Select(attrs={'class': 'form-control', 'id': 'region_select'}),
            'id_comuna': forms.Select(attrs={'class': 'form-control', 'id': 'comuna_select'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(InmuebleForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control' 

class SolicitudForm(forms.Form):
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu mensaje aquí...',
            'rows': 5
        }),
        label='Mensaje',
        max_length=500
    )