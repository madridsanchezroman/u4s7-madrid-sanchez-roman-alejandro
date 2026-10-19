
# path: permite crear rutas para las paginas

from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.inicio, name='inicio'),

    # Listado de servicios
    path('servicios/', views.servicios, name='servicios'),

    # Crear un servicio
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),

    # Editar un servicio
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),

    # Eliminar un servicio
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),

    # Registrar nuevos usuarios
    path('registro/', views.registro, name='registro'),

    # Iniciar sesión
    path('login/', views.iniciar_sesion, name='login'),

    # Cerrar sesión
    path('logout/', views.cerrar_sesion, name='logout'),
]

