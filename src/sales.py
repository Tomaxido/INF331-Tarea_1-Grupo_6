from __future__ import annotations
from typing import List, Dict
from .logging_conf import logger

def vender_interactivo(eventos: List[Dict], idx: int):
    ev = eventos[idx]
    if ev["cupos"] <= 0:
        print("No hay cupos disponibles.")
        logger.warning("Venta rechazada (sin cupos): %s", (ev["nombre"], ev["fecha"], ev["categoria"]))
        return
    ev["cupos"] -= 1
    logger.info("Venta realizada: %s", (ev["nombre"], ev["fecha"], ev["categoria"]))
    print(f"Venta OK. Cupos restantes: {ev['cupos']}")