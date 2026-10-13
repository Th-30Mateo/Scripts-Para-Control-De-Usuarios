# Scripts para Control de Usuarios

Programa de consola desarrollado en Python para practicar la administración de registros de usuarios mediante operaciones CRUD: crear, consultar, actualizar y eliminar.

## Funcionalidades

- Crear registros de usuarios.
- Listar los usuarios registrados.
- Buscar usuarios por nombre de usuario o identificador.
- Editar información de usuarios.
- Eliminar registros mediante confirmación.
- Generar usuarios de ejemplo de forma aleatoria.
- Mostrar estadísticas sencillas sobre los roles registrados.
- Seleccionar y mostrar un usuario aleatorio.

## Tecnologías y conceptos

- Python
- Listas y diccionarios
- Funciones
- Validaciones y manejo de entradas
- Menús interactivos por consola
- Estructuras condicionales y control de flujo

## Ejecución

Cloná el repositorio:

```bash
git clone https://github.com/Th-30Mateo/Scripts-Para-Control-De-Usuarios.git
cd Scripts-Para-Control-De-Usuarios
```

El archivo Python se encuentra dentro de directorios anidados. Localizá `PUNTO4.PY` y ejecutalo:

```bash
python PUNTO4.PY
```

Si utilizás Linux o WSL, podés reemplazar `python` por `python3` cuando corresponda.

## Almacenamiento

Los usuarios se mantienen en estructuras de datos en memoria. Los cambios no se conservan al cerrar el programa.

## Mejoras pendientes

- Corregir y centralizar las validaciones de entradas.
- Gestionar correctamente los identificadores y evitar registros inconsistentes.
- Manejar los errores al convertir valores introducidos por el usuario.
- Evitar fallos cuando no existen usuarios registrados.
- Mejorar la organización de los archivos y directorios.
- Incorporar persistencia si el alcance futuro del proyecto lo requiere.

## Objetivo de aprendizaje

Practicar la programación estructurada, la manipulación de colecciones, las funciones y el diseño de una interfaz de consola interactiva.

Este programa es un ejercicio educativo y no administra cuentas reales del sistema operativo.
