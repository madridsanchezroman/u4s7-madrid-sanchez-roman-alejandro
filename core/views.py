
# render: combina una plantilla con datos
# redirect: redirige a otra pagina
# get_object_or_404: busca un registro o muestra error 404

from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Servicio
from .forms import ServicioForm



# Vista de inicio de la Semana 3
def inicio(request):
    # Obtiene la informacion de la base de datos
    info_bd = connection.settings_dict

    # Datos que se envian a la plantilla
    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }

    # Muestra la pagina de inicio
    return render(request, 'core/inicio.html', contexto)


# Mostrar solamente los servicios del usuario actual
@login_required
def servicios(request):

    # Filtrar los servicios por el usuario que inició sesión
    lista_servicios = Servicio.objects.filter(
        propietario=request.user
    )

    # Mostrar los servicios del usuario
    return render(
        request,
        'core/servicios.html',
        {'servicios': lista_servicios}
    )


# Exige iniciar sesión para crear servicios
@login_required
def crear_servicio(request):

    # Comprueba si el usuario envió el formulario
    if request.method == 'POST':
        form = ServicioForm(request.POST)

        # Valida los datos del formulario
        if form.is_valid():

            # Crea el servicio sin guardarlo todavía
            servicio = form.save(commit=False)

            # Asigna el usuario que inició sesión
            servicio.propietario = request.user

            # Guarda el servicio en MySQL
            servicio.save()

            # Regresa al listado
            return redirect('servicios')

    else:
        # Muestra el formulario vacío
        form = ServicioForm()

    # Muestra la página de creación
    return render(request, 'core/servicio_form.html', {
        'form': form,
        'titulo_pagina': 'Nuevo servicio'
    })


# Exige que el usuario inicie sesion para editar
@login_required
def editar_servicio(request, pk):

    # Busca el servicio por su ID
    servicio = get_object_or_404(Servicio, pk=pk, propietario=request.user)
    # Comprueba si el usuario envio cambios
    if request.method == 'POST':

        # Carga los datos nuevos sobre el servicio existente
        form = ServicioForm(request.POST, instance=servicio)

        # Comprueba que los datos sean validos
        if form.is_valid():

            # Guarda los cambios en MySQL
            form.save()

            # Regresa al listado de servicios
            return redirect('servicios')

    else:
        # Muestra el formulario con los datos actuales
        form = ServicioForm(instance=servicio)

    # Utiliza el mismo formulario de crear servicios
    return render(request, 'core/servicio_form.html', {
        'form': form,
        'titulo_pagina': 'Editar servicio'
    })


# Exige que el usuario inicie sesion para eliminar
@login_required
def eliminar_servicio(request, pk):

    # Busca el servicio por su ID
    servicio = get_object_or_404(Servicio, pk=pk, propietario=request.user)

    # Solo elimina cuando el usuario confirma
    if request.method == 'POST':

        # Elimina el servicio de MySQL
        servicio.delete()

        # Regresa al listado de servicios
        return redirect('servicios')

    # Muestra la pantalla para confirmar
    return render(request, 'core/servicio_confirm_delete.html', {
        'servicio': servicio
    })


# Vista para registrar nuevos usuarios
def registro(request):
    # Si el usuario envió el formulario
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # Validar los datos
        if form.is_valid():
            # Guardar el nuevo usuario
            usuario_nuevo = form.save()

            # Iniciar sesión automáticamente
            login(request, usuario_nuevo)

            # Mostrar mensaje de bienvenida
            messages.success(
                request,
                f'Cuenta creada. ¡Bienvenido, {usuario_nuevo.username}!'
            )

            # Redirigir al listado de servicios
            return redirect('servicios')
    else:
        # Mostrar formulario vacío
        form = UserCreationForm()

    # Mostrar la página de registro
    return render(request, 'core/registro.html', {'form': form})


# Vista para iniciar sesión
def iniciar_sesion(request):
    # Si el usuario envió el formulario
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        # Validar usuario y contraseña
        if form.is_valid():
            # Iniciar sesión
            login(request, form.get_user())

            # Mostrar mensaje de éxito
            messages.success(
                request,
                'Sesión iniciada correctamente.'
            )

            # Redirigir al listado de servicios
            return redirect('servicios')
    else:
        # Mostrar formulario vacío
        form = AuthenticationForm()

    # Mostrar la página de inicio de sesión
    return render(request, 'core/login.html', {'form': form})


# Vista para cerrar sesión
def cerrar_sesion(request):
    # Cerrar la sesión del usuario
    logout(request)

    # Mostrar mensaje de confirmación
    messages.info(
        request,
        'Sesión cerrada correctamente.'
    )

    # Redirigir a la página de login
    return redirect('login')



