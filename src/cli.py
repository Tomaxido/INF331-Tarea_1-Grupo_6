from __future__ import annotations
from getpass import getpass

from .logging_conf import logger
from .auth import login
from .storage import load_data, save_data, path_data_file
from .events import listar_eventos, mostrar_evento, crear_evento_interactivo, editar_evento_interactivo, eliminar_evento_interactivo, buscar_interactivo
from .sales import vender_interactivo, devolver_interactivo

def pause():
    input("\nPresiona ENTER para continuar...")


def header(title: str):
    print("\n" + "="*60)
    print(title)
    print("="*60)


def menu() -> int:
    print("\nMenú")
    print("1) Crear evento")
    print("2) Listar eventos")
    print("3) Buscar (nombre/fecha/categoría)")
    print("4) Detalle / Editar evento")
    print("5) Eliminar evento")
    print("6) Vender entrada")
    print("7) Devolver entrada")
    print("8) Generar reporte")
    print("9) Guardar y salir")
    choice = input("Elige una opción: ").strip()
    try:
        return int(choice)
    except ValueError:
        return -1


def do_login() -> bool:
    print("=== Autenticación requerida ===")
    user = input("Usuario: ").strip()
    pwd = getpass("Contraseña: ").strip()
    ok = login(user, pwd)
    if ok:
        logger.info("Login OK para usuario '%s'", user)
        print("Login exitoso.\n")
    else:
        logger.warning("Intento de login FALLIDO para usuario '%s'", user)
        print("Credenciales inválidas.\n")
    return ok


def main():
    header("Gestión de Micro-Eventos (CLI)")
    if not do_login():
        return

    eventos = load_data()

    while True:
        op = menu()
        if op == 1:
            header("Crear evento")
            crear_evento_interactivo(eventos)
            pause()
            
        elif op == 2: 
            header("Lista de eventos")
            listar_eventos(eventos)
            pause()
        
        elif op == 3:
            header("Búsquedas")
            buscar_interactivo(eventos)
            pause()

        elif op == 4: 
            header("Detalle de un evento")
            listar_eventos(eventos)
            if not eventos:
                pause()
                continue
            try:
                idx = int(input("Índice de evento a detallar/editar: "))
                mostrar_evento(eventos, idx)
                ans = input("¿Editar este evento? (s/n): ").strip().lower()
                if ans == "s":
                    editar_evento_interactivo(eventos, idx)
            except (ValueError, IndexError):
                print("Índice inválido.")
            pause()
            
        elif op == 5:
            header("Eliminar evento")
            listar_eventos(eventos)
            if not eventos:
                pause()
                continue
            try:
                idx = int(input("Índice a eliminar: "))
                eliminar_evento_interactivo(eventos, idx)
            except (ValueError, IndexError):
                print("Índice inválido.")
            pause()
        
        elif op == 6:
            header("Vender entrada")
            listar_eventos(eventos)
            if not eventos:
                pause()
                continue
            try:
                idx = int(input("Índice para vender: "))
                vender_interactivo(eventos, idx)
            except (ValueError, IndexError):
                print("Índice inválido.")
            pause()

        elif op == 7:
            header("Devolver entrada")
            listar_eventos(eventos)
            if not eventos:
                pause()
                continue
            try:
                idx = int(input("Índice para devolver: "))
                devolver_interactivo(eventos, idx)
            except (ValueError, IndexError):
                print("Índice inválido.")
            pause()

        elif op == 9:
            save_data(eventos)
            print(f"Datos guardados en {path_data_file()}")
            print("¡Hasta luego!")
            break

        elif op == -1:
            print("Opción inválida.")
        else:
            print(f"(skeleton/login) elegiste opción {op}, aún no implementada.")
            pause()


if __name__ == "__main__":
    main()
