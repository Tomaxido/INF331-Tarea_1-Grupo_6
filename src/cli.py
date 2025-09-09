# cli.py con login habilitado
from __future__ import annotations
from getpass import getpass

from .logging_conf import logger
from .auth import login

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

    while True:
        op = menu()

        if op == 9:
            print("¡Hasta luego!")
            break
        elif op == -1:
            print("Opción inválida.")
        else:
            print(f"(skeleton/login) elegiste opción {op}, aún no implementada.")
        pause()

if __name__ == "__main__":
    main()
