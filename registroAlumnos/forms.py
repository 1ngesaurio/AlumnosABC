from django import forms
from django.core.validators import RegexValidator
from .models import Alumno
from django.forms.widgets import DateInput

class AlumnoForm(forms.ModelForm):
    carnet_validator = RegexValidator(
        regex=r'^\d{4}-\d{2}-\d{4}$',
        message="El formato del carnet debe ser 'XXXX-XX-XXXX'."
    )
    carnet = forms.CharField(validators=[carnet_validator], max_length=14)

    class Meta:
        model = Alumno
        fields = ['carnet', 'nombres', 'apellidos', 'correoElectronico', 'fechaNacimiento']
        widgets = {
            'fechaNacimiento': DateInput(attrs={'type': 'date'}),
        }
        error_messages = {
            'carnet': {
                'unique': ("Un alumno con este Carnet ya existe."),
            },
            'correoElectronico': {
                'unique': ("Un alumno con este Correo Electrónico ya existe."),
            },
        }

