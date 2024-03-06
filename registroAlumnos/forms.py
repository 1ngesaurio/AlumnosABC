from django import forms
from django.forms import DateInput
from django.core.validators import RegexValidator
from .models import Alumno

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
            'fechaNacimiento': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }
        input_formats = {
            'fechaNacimiento': ['%d/%m/%Y'],
        }
        error_messages = {
            'carnet': {
                'unique': ("Un alumno con este Carnet ya existe."),
            },
            'correoElectronico': {
                'unique': ("Un alumno con este Correo Electrónico ya existe."),
            },
        }
