from django.contrib import admin
from django.urls import path, include
from registroAlumnos import views as registroAlumnos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registroAlumnos_views.lista_alumnos, name='lista'),  # Ruta base
    path('registroAlumnos/', include('registroAlumnos.urls')),  # Incluyendo las URLs de la aplicación
]

