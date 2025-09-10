from __future__ import annotations
from typing import List, Dict

def generar_reporte(eventos: List[Dict]) -> Dict[str, int]:
    total = len(eventos)
    suma_cupos = sum(e["cupos"] for e in eventos)
    agotados = sum(1 for e in eventos if e["cupos"] == 0)
    return {"total_eventos": total, "suma_cupos": suma_cupos, "eventos_agotados": agotados}

def imprimir_reporte(rep: Dict[str, int]):
    print(f"Total de eventos: {rep['total_eventos']}")
    print(f"Suma de cupos disponibles: {rep['suma_cupos']}")
    print(f"Eventos agotados: {rep['eventos_agotados']}")
