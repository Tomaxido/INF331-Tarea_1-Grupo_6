from __future__ import annotations
from dataclasses import dataclass
from typing import Dict

ALLOWED_CATEGORIES = {"charlas", "talleres", "shows"}

@dataclass
class Evento:
    nombre: str
    descripcion: str
    fecha: str          # YYYY-MM-DD
    categoria: str      # charlas | talleres | shows
    cupos: int          # disponibles actuales
    cupos_max: int      # tope para devoluciones

    def to_dict(self) -> Dict:
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "fecha": self.fecha,
            "categoria": self.categoria,
            "cupos": self.cupos,
            "cupos_max": self.cupos_max,
        }
