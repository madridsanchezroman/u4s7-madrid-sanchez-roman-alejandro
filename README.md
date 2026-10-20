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
│   ├
