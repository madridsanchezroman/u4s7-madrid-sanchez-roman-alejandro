# Unidad 4 - Semana 7: Pulido funcional, UX y defensa

## Aplicaciones Web - Django

**Alumno:** Madrid Sánchez Román Alejandro  
**Práctica:** Unidad 4, Semana 7  
**Proyecto:** Sistema de Gestión de Servicios  
**Repositorio:** [GitHub - Semana 7](https://github.com/madridsanchezroman/u4s7-madrid-sanchez-roman-alejandro)

## Descripción del proyecto

Este proyecto consiste en una aplicación web desarrollada con Django y conectada a una base de datos MySQL alojada en Aiven.

El sistema permite administrar servicios mediante operaciones CRUD, además de contar con registro de usuarios, inicio de sesión y protección de la información de cada usuario.

En la Semana 7 se realizaron mejoras para facilitar el uso del sistema, agregando búsqueda de servicios, paginación y ajustes en la interfaz para dispositivos móviles.

## Tecnologías utilizadas

- Python
- Django 6.1.1
- MySQL 8.4
- Aiven (base de datos en la nube)
- HTML y Tailwind CSS
- Git y GitHub
- Render (despliegue web)

## Funcionalidades del sistema

### 1. Autenticación de usuarios
- Registro de nuevos usuarios.
- Inicio y cierre de sesión.
- Protección de vistas mediante `login_required`.
- Cada usuario puede administrar sus propios servicios.

### 2. CRUD de servicios
- Crear nuevos servicios.
- Consultar servicios registrados.
- Editar información y precios.
- Eliminar servicios mediante confirmación.
- Guardar información en MySQL de Aiven.

### 3. Búsqueda de servicios
- Buscar servicios mediante su título.
- Búsqueda sin distinguir entre mayúsculas y minúsculas.
- Mostrar mensajes cuando no se encuentran resultados.
- Opción para quitar el filtro de búsqueda.

### 4. Paginación
- Mostrar un máximo de 5 servicios por página.
- Navegar entre páginas mediante los botones Anterior y Siguiente.
- Mantener la búsqueda al cambiar de página.
- Ordenar los servicios del más reciente al más antiguo.

### 5. Mejoras de interfaz y experiencia de usuario
- Diseño adaptable a celulares.
- Tabla con desplazamiento horizontal en pantallas pequeñas.
- Navegación mediante teclado.
- Mensajes cuando no existen servicios registrados.
- Botones para crear, editar y eliminar servicios.

## Seguridad

El sistema utiliza las herramientas de seguridad proporcionadas por Django.

- Autenticación y control de sesiones.
- Restricción de acceso a operaciones protegidas.
- Verificación del propietario de los servicios.
- Protección CSRF en formularios.
- Uso de variables de entorno para credenciales.

El archivo `.env` no se incluye en el repositorio por seguridad.

## Estructura del proyecto

```text
miproyecto-django_MSRA/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── base.html
│   │       ├── inicio.html
│   │       ├── login.html
│   │       ├── registro.html
│   │       ├── servicios.html
│   │       ├── servicio_form.html
│   │       └── servicio_confirm_delete.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── miproyecto_MSRA/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Ejecución local

Activar el entorno virtual en Windows:

```powershell
.\env\Scripts\Activate.ps1
```

Instalar las dependencias del proyecto:

```powershell
pip install -r requirements.txt
```

Configurar las variables de entorno necesarias para MySQL y Django.

Comprobar la configuración:

```powershell
python manage.py check
```

Iniciar el servidor:

```powershell
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Pruebas realizadas

Durante la Semana 7 se realizaron las siguientes pruebas:

- Conexión con MySQL de Aiven.
- Funcionamiento del servidor Django.
- Registro y consulta de servicios.
- Edición y eliminación de servicios.
- Búsqueda por título.
- Búsqueda sin resultados.
- Paginación de cinco registros.
- Navegación entre páginas.
- Visualización en pantalla móvil de 375 px.
- Navegación mediante teclado.

Las pruebas locales permitieron comprobar el funcionamiento de las principales operaciones del sistema.

## Repositorio GitHub

[Unidad 4 Semana 7 - Madrid Sánchez Román Alejandro](https://github.com/madridsanchezroman/u4s7-madrid-sanchez-roman-alejandro)

## Conclusión

En esta práctica se mejoró el funcionamiento y la presentación del sistema de gestión de servicios desarrollado con Django.

La búsqueda y paginación permiten encontrar y consultar la información de manera más sencilla, mientras que los ajustes de interfaz hacen que la aplicación sea más cómoda de utilizar en diferentes dispositivos.

También se realizaron pruebas para comprobar el funcionamiento del CRUD, la autenticación y la conexión con la base de datos MySQL de Aiven.

Con estas mejoras, el sistema queda preparado para continuar con la etapa final de presentación y despliegue.

---

**Madrid Sánchez Román Alejandro**  
**Unidad 4 - Semana 7**
