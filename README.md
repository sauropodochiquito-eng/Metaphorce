# Sistema de Gestion de Notas Personales en Consola

Programa de consola en Python para crear, editar, eliminar, listar y buscar notas personales. Las notas se guardan en un archivo JSON para que no se pierdan al cerrar el programa.

## Requisitos

Python 3.8 o superior. No usa librerias externas, solo las que ya vienen con Python (json, os, datetime).

## Archivos del proyecto

- notas.py: el programa
- notas.json: donde se guardan las notas
- README.md: este archivo

## Como ejecutarlo

```
python notas.py
```

Si eso no funciona (por ejemplo en Mac o Linux), probar con:

```
python3 notas.py
```

## Como se usa

Al correr el programa aparece un menu:

```

SISTEMA DE GESTION DE NOTAS PERSONALES

1. Agregar nota
2. Editar nota
3. Eliminar nota
4. Listar notas
5. Buscar nota
6. Salir

Elige una opcion (1-6):
```

Se elige un numero del 1 al 6 y Enter.

**Agregar nota**: pide titulo, contenido y categoria. Si el titulo o el contenido quedan vacios, no se guarda la nota. Si la categoria se deja vacia, se guarda como "Sin categoria".

Ejemplo:
```
Elige una opcion (1-6): 1

    Agregar nota    
Titulo: Reunion de equipo
Contenido: Preparar el informe antes del viernes
Categoria (Trabajo, Personal, Estudio...): Trabajo
Nota agregada con ID 3
```

**Editar nota**: muestra la lista de notas, pide el ID de la que se quiere editar, y despues pide el nuevo titulo, contenido y categoria (se puede dejar vacio para no cambiar ese campo).

**Eliminar nota**: pide el ID y confirma con s/n antes de borrar.

**Listar notas**: muestra todas las notas con su ID, titulo, categoria, fecha y contenido.

**Buscar nota**: pide una palabra y busca coincidencias en el titulo, el contenido o la categoria de todas las notas.

Ejemplo:
```
Elige una opcion (1-6): 5
Palabra clave o categoria a buscar: trabajo
Se encontraron 1 nota(s):

ID: 3
Titulo: Reunion de equipo
Categoria: Trabajo
Fecha: 2026-08-28 10:15:00
Contenido: Preparar el informe antes del viernes
```

## Como se guardan los datos

Cada nota es un diccionario con estos campos: id, titulo, contenido, fecha_creacion, categoria. Se guardan en notas.json, por ejemplo:

```json
[
    {
        "id": 1,
        "titulo": "Bienvenida",
        "contenido": "Esta es una nota de ejemplo...",
        "fecha_creacion": "2026-08-28 09:00:00",
        "categoria": "Personal"
    }
]
```

Si notas.json no existe todavia, el programa lo crea solo cuando agregas la primera nota.

## Manejo de errores

- Si notas.json no existe, el programa avisa y arranca con una lista vacia en vez de fallar.
- Si notas.json esta corrupto o mal escrito, tambien avisa y arranca con una lista vacia.
- Si el titulo o contenido de una nota nueva estan vacios, se cancela y no se guarda nada.
- Si al editar o eliminar el ID no existe o no es un numero, se avisa y no pasa nada.


## Autor

Claudio Alessandro Juárez López
