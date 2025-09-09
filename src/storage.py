from __future__ import annotations
import json, os
from typing import List, Dict
from .logging_conf import logger

_DATA_FILE = "data.json"

def path_data_file() -> str:
    return os.path.abspath(_DATA_FILE)

def load_data() -> List[Dict]:
    if os.path.exists(_DATA_FILE):
        with open(_DATA_FILE, "r", encoding="utf-8") as f:
            eventos = json.load(f)
        logger.info("Datos cargados desde %s", path_data_file())
        return eventos

    eventos = [
        {
            "nombre": "charla1",
            "descripcion": "Descripción de la charla 1",
            "fecha": "2025-02-20",
            "categoria": "charlas",
            "cupos": 30,
            "cupos_max": 30,
        },
        {
            "nombre": "charla2",
            "descripcion": "Descripción de la charla 2",
            "fecha": "2025-02-21",
            "categoria": "charlas",
            "cupos": 25,
            "cupos_max": 25,
        },
    ]
    logger.info("Datos de ejemplo cargados (no se encontró data.json)")
    return eventos

def save_data(eventos: List[Dict]):
    with open(_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(eventos, f, ensure_ascii=False, indent=2)
    logger.info("Datos guardados en %s", path_data_file())
