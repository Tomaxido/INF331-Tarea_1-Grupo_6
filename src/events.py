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
