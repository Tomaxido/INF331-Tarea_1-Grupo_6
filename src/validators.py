from __future__ import annotations
from typing import List, Dict, Optional
from datetime import datetime

def normaliza_texto(s: str) -> str:
    return " ".join(s.strip().split())

def normaliza_cat(c: str) -> str:
    return normaliza_texto(c).lower()

def valida_fecha_iso(fecha: str) -> bool:
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def clave_compuesta(e: Dict) -> tuple[str, str, str]:
    return (normaliza_texto(e["nombre"]).lower(), e["fecha"], normaliza_cat(e["categoria"]))

def es_unico(eventos: List[Dict], e: Dict, idx_excluir: Optional[int] = None) -> bool:
    key = clave_compuesta(e)
    for i, ev in enumerate(eventos):
        if idx_excluir is not None and i == idx_excluir:
            continue
        if clave_compuesta(ev) == key:
            return False
    return True
