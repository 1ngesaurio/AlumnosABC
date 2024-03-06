from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alumnos, name='lista_alumnos'),
    path('alta/', views.alta_alumno, name='alta_alumno'),
    path('baja/<int:pk>/', views.baja_alumno, name='baja_alumno'),
    path('cambio/<int:pk>/', views.cambio_alumno, name='cambio_alumno'),
    path('dashboard/', views.dashboard_view, name='dashboard_views'),
]
