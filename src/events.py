from __future__ import annotations
from typing import List, Dict
from .validators import (
    valida_fecha_iso, normaliza_texto, normaliza_cat,
    es_unico, clave_compuesta
)
from .logging_conf import logger

def mostrar_evento(eventos: List[Dict], idx: int):
   
    ev = eventos[idx]
    print(f"[{idx}] {ev['nombre']} ({ev['categoria']}) - {ev['fecha']}")
    print(f"    {ev['descripcion']}")
    print(f"    Cupos: {ev['cupos']} / {ev['cupos_max']}")

def listar_eventos(eventos: List[Dict]):

    if not eventos:
        print("No hay eventos registrados.")
        return
    for i, _ in enumerate(eventos):
        mostrar_evento(eventos, i)
        
def crear_evento_interactivo(eventos: List[Dict]):
    """Crea un nuevo evento interactivo, validando duplicados"""
    nombre = normaliza_texto(input("Nombre: "))
    descripcion = input("Descripción: ").strip()
    fecha = input("Fecha (YYYY-MM-DD): ").strip()
    categoria = normaliza_cat(input("Categoría (charlas/talleres/shows): "))
    try:
        cupos = int(input("Cupos (>=0): ").strip())
    except ValueError:
        print("Cupos inválidos.")
        return
    if cupos < 0:
        print("Cupos no puede ser negativo.")
        return

    if not valida_fecha_iso(fecha):
        print("Fecha inválida. Formato esperado YYYY-MM-DD.")
        return

    e = {
        "nombre": nombre,
        "descripcion": descripcion,
        "fecha": fecha,
        "categoria": categoria,
        "cupos": cupos,
        "cupos_max": cupos,
    }

    if not es_unico(eventos, e):
        print("ERROR: ya existe un evento con ese (nombre, fecha, categoría).")
        logger.warning("Intento de alta duplicada: %s", clave_compuesta(e))
        return

    eventos.append(e)
    logger.info("Evento creado: %s", clave_compuesta(e))
    print("Evento creado correctamente.")

def editar_evento_interactivo(eventos: List[Dict], idx: int):
    ev = eventos[idx]
    print("Dejar vacío para mantener el valor actual.")

    nombre = input(f"Nombre [{ev['nombre']}]: ").strip()
    descripcion = input(f"Descripción [{ev['descripcion']}]: ").strip()
    fecha = input(f"Fecha [{ev['fecha']}]: ").strip()
    categoria = input(f"Categoría [{ev['categoria']}]: ").strip()
    cupos_str = input(f"Cupos [{ev['cupos']}]: ").strip()

    nuevo = dict(ev)  # copia del evento actual

    if nombre:
        nuevo["nombre"] = normaliza_texto(nombre)
    if descripcion:
        nuevo["descripcion"] = descripcion
    if fecha:
        if not valida_fecha_iso(fecha):
            print("Fecha inválida.")
            return
        nuevo["fecha"] = fecha
    if categoria:
        nuevo["categoria"] = normaliza_cat(categoria)
    if cupos_str:
        try:
            cupos = int(cupos_str)
        except ValueError:
            print("Cupos inválidos.")
            return
        if cupos < 0:
            print("Cupos no puede ser negativo.")
            return
        if cupos > ev["cupos_max"]:
            nuevo["cupos_max"] = cupos  # ampliar máximo
        nuevo["cupos"] = cupos

    if not es_unico(eventos, nuevo, idx_excluir=idx):
        print("ERROR: la edición genera duplicado (nombre, fecha, categoría).")
        logger.warning("Intento de edición duplicada: %s", clave_compuesta(nuevo))
        return

    eventos[idx] = nuevo
    logger.info("Evento editado: %s", clave_compuesta(nuevo))
    print("Evento actualizado.")