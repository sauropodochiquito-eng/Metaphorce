import json
import os
import sys
from datetime import datetime

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ARCHIVO_NOTAS = "notas.json"



def cargar_notas():
    if not os.path.exists(ARCHIVO_NOTAS):
        print(f"¡No se encontró !'{ARCHIVO_NOTAS}'. Se creará uno nuevo al agregar la primera nota.")
        return []

    try:
        with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except json.JSONDecodeError:
        print(f"El archivo '{ARCHIVO_NOTAS}' está dañado o mal formado. Se iniciará con una lista vacía.")
        return []
    except OSError as error:
        print(f"No se pudo leer '{ARCHIVO_NOTAS}': {error}. Se iniciará con una lista vacía.")
        return []


def guardar_notas(notas):
    try:
        with open(ARCHIVO_NOTAS, "w", encoding="utf-8") as archivo:
            json.dump(notas, archivo, indent=4, ensure_ascii=False)
    except OSError as error:
        print(f"No se pudieron guardar los cambios en '{ARCHIVO_NOTAS}': {error}")


def generar_id(notas):
    if not notas:
        return 1
    return max(nota["id"] for nota in notas) + 1


def agregar_nota(notas):
    print("\n--- Agregar Nueva Nota ---")

    titulo = input("Título: ").strip()
    if not titulo:
        print("El título no puede estar vacío. Operación cancelada.")
        return

    contenido = input("Contenido: ").strip()
    if not contenido:
        print("El contenido no puede estar vacío. Operación cancelada.")
        return

    categoria = input("Categoría (ej. Trabajo, Personal, Estudio): ").strip()
    if not categoria:
        categoria = "Sin categoría"

    nueva_nota = {
        "id": generar_id(notas),
        "titulo": titulo,
        "contenido": contenido,
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "categoria": categoria,
    }

    notas.append(nueva_nota)
    guardar_notas(notas)
    print(f"Nota '{titulo}' agregada correctamente con ID {nueva_nota['id']}.")


def listar_notas(notas):
    print("\n--- Listado de Notas ---")
    if not notas:
        print("No hay notas guardadas todavía.")
        return

    for nota in notas:
        _imprimir_nota(nota)


def buscar_notas(notas):
    print("\n    Buscar Notas    ")
    if not notas:
        print("No hay notas guardadas todavía.")
        return

    termino = input("Ingresa una palabra clave o categoría a buscar: ").strip().lower()
    if not termino:
        print("Debes ingresar un término de búsqueda.")
        return

    resultados = [
        nota for nota in notas
        if termino in nota["titulo"].lower()
        or termino in nota["contenido"].lower()
        or termino in nota["categoria"].lower()
    ]

    if not resultados:
        print(f"No se encontraron notas relacionadas con '{termino}'.")
        return

    print(f"\nSe encontraron {len(resultados)} nota(s):")
    for nota in resultados:
        _imprimir_nota(nota)


def editar_nota(notas):
    print("\n    Editar Nota    ")
    if not notas:
        print("No hay notas guardadas todavía.")
        return

    listar_notas(notas)
    id_nota = input("\nIngresa el ID de la nota a editar: ").strip()

    if not id_nota.isdigit():
        print("ID inválido. Debe ser un número entero.")
        return

    nota = _buscar_por_id(notas, int(id_nota))
    if nota is None:
        print(f"No se encontró ninguna nota con ID {id_nota}.")
        return

    print("\nDeja un campo en blanco y presiona Enter para conservar su valor actual.")
    nuevo_titulo = input(f"Nuevo título [{nota['titulo']}]: ").strip()
    nuevo_contenido = input(f"Nuevo contenido [{nota['contenido']}]: ").strip()
    nueva_categoria = input(f"Nueva categoría [{nota['categoria']}]: ").strip()

    if nuevo_titulo:
        nota["titulo"] = nuevo_titulo
    if nuevo_contenido:
        nota["contenido"] = nuevo_contenido
    if nueva_categoria:
        nota["categoria"] = nueva_categoria

    guardar_notas(notas)
    print(f"Nota con ID {nota['id']} actualizada correctamente.")


def eliminar_nota(notas):
    print("\n    Eliminar Nota    ")
    if not notas:
        print("No hay notas guardadas todavía.")
        return

    listar_notas(notas)
    id_nota = input("\nIngresa el ID de la nota a eliminar: ").strip()

    if not id_nota.isdigit():
        print("ID inválido. Debe ser un número entero.")
        return

    nota = _buscar_por_id(notas, int(id_nota))
    if nota is None:
        print(f"No se encontró ninguna nota con ID {id_nota}.")
        return

    confirmacion = input(f"¿Seguro que deseas eliminar '{nota['titulo']}'? (s/n): ").strip().lower()
    if confirmacion == "s":
        notas.remove(nota)
        guardar_notas(notas)
        print("Nota eliminada correctamente.")
    else:
        print("Operación cancelada.")


def _buscar_por_id(notas, id_nota):
    return next((nota for nota in notas if nota["id"] == id_nota), None)


def _imprimir_nota(nota):
    print(f"\nID: {nota['id']}")
    print(f"Título: {nota['titulo']}")
    print(f"Categoría: {nota['categoria']}")
    print(f"Fecha de creación: {nota['fecha_creacion']}")
    print(f"Contenido: {nota['contenido']}")
    print("\n ")

def mostrar_menu():
    print("\n ")
    print("SISTEMA DE GESTIÓN DE NOTAS PERSONALES")
    print("\n ")
    print("1. Agregar nota")
    print("2. Editar nota")
    print("3. Eliminar nota")
    print("4. Listar notas")
    print("5. Buscar nota")
    print("6. Salir")
    print("\n ")


def main():
    notas = cargar_notas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            agregar_nota(notas)
        elif opcion == "2":
            editar_nota(notas)
        elif opcion == "3":
            eliminar_nota(notas)
        elif opcion == "4":
            listar_notas(notas)
        elif opcion == "5":
            buscar_notas(notas)
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema de notas! Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor selecciona un número del 1 al 6.")


if __name__ == "__main__":
    main()
