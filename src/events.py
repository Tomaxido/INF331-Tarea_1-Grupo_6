# src/events.py
from __future__ import annotations
from typing import List, Dict

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
