# INF331 – Tarea 1 – Grupo 6
# Gestión de Micro-Eventos (CLI en Python)

> Aplicación de consola para administrar micro-eventos con **CRUD**, **búsquedas** por nombre/fecha/categoría y **reporte on-demand** (total de eventos, suma de cupos disponibles y eventos agotados). Incluye autenticación básica, logging y persistencia simple en JSON.

---

## 📛 Nombre
**Gestión de Micro-Eventos (CLI en Python)**

## 📝 Descripción
Este proyecto implementa una aplicación **CLI** que permite a un administrador gestionar eventos de forma simple:
- **CRUD de eventos** con **unicidad** por `(nombre, fecha, categoría)`.
- **Búsquedas** por nombre (substring), fecha exacta (`YYYY-MM-DD`) y categoría.
- **Ventas y devoluciones** con control de **cupos** y **cupos_max** (no baja de 0 ni sube del máximo).
- **Reporte bajo demanda** con 3 métricas: total de eventos, suma de cupos disponibles y eventos agotados.
- **Autenticación** mediante variables de entorno (`ADMIN_USER`, `ADMIN_PASS`).
- **Logs** a `app.log`.
- **Persistencia simulada**: los datos viven en memoria y se guardan/cargan desde `data.json`.

> Pensado como MVP educativo: sin dependencias externas, sólo **Python 3.10+**.

---

## ⚙️ Instalación

### Requisitos
- Python **3.10+**

### Pasos
```bash
# 1) Clonar el repositorio
git clone <URL_DEL_REPO>
cd INF331-Tarea_1-Grupo_6

# 2) No hay dependencias a instalar (stdlib solamente)

# 3) (Opcional) Para definir credenciales del admin, ejecutar:
# Windows PowerShell
$env:ADMIN_USER="admin"; $env:ADMIN_PASS="admin"
# Linux/Mac
export ADMIN_USER=admin ADMIN_PASS=admin
```

---

## ▶️ Ejecutar
```bash
python -m src.cli
```

---

## ▶️ Cómo usar

### Flujo general
1. **Login** con `ADMIN_USER/ADMIN_PASS`. Por defecto ambos son `admin` si no defines variables de entorno.
2. Menú principal:
   - **1)** Crear evento
   - **2)** Listar eventos
   - **3)** Buscar (nombre/fecha/categoría)
   - **4)** Detalle / Editar evento
   - **5)** Eliminar evento
   - **6)** Vender entrada
   - **7)** Devolver entrada
   - **8)** Generar reporte
   - **9)** Guardar y salir

### Reglas clave
- **Unicidad**: no se permite duplicar `(nombre, fecha, categoría)` (case-insensitive para nombre y categoría).
- **Venta**: sólo si `cupos > 0` → `cupos -= 1`.
- **Devolución**: sólo si `cupos < cupos_max` → `cupos += 1`.
- **Reporte**: muestra total de eventos, suma de cupos y cantidad de eventos agotados.
- **Persistencia**: al elegir **“Guardar y salir”** se actualiza `data.json`. En el primer arranque, si `data.json` no existe, se cargan **datos de ejemplo**.

---

## 🤝 Cómo contribuir

Usamos un **Mini-GitFlow** simple para 2 personas:
- **main**: versión estable (taggeada). No se commitea directo.
- **develop**: rama de integración.
- **feature/***: trabajo por tema. Siempre nace desde `develop` y se fusiona vía **PR** hacia `develop`.

### Convenciones de commits (Conventional Commits)
- `feat: ...` nueva funcionalidad
- `fix: ...` corrección de bug
- `docs: ...` documentación
- `chore: ...` tareas de mantenimiento (p. ej., logger, .gitignore)
- `refactor: ...` cambios internos sin alterar comportamiento
- `test: ...` pruebas

### Revisión / PR checklist
- La app corre con `python -m src.cli`.
- Se probaron las rutas del menú afectadas por la feature.
- No se versionan `data.json` ni `app.log` (ver `.gitignore`).
- Se actualizó documentación si aplica (`README.md`, `docs/manual_tests.md`).

> Para una primera release: crear `release/0.1.0`, merge **no-ff** a `main`, crear **tag** `v0.1.0`, y merge de vuelta a `develop`.

---

## 📄 Licencia

Este proyecto se distribuye bajo la **Licencia MIT**.  

```
MIT License

Copyright (c) 2025 INF331 - Grupo 6

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🗂️ Estructura del proyecto

```
/INF331-Tarea_1-Grupo_6
  ├─ src/
  │   ├─ cli.py              # menú y loop principal
  │   ├─ auth.py             # login con variables de entorno
  │   ├─ models.py           # dataclass y categorías (referencial)
  │   ├─ storage.py          # cargar/guardar JSON + seed
  │   ├─ validators.py       # normalización, fecha ISO, clave compuesta
  │   ├─ events.py           # CRUD + búsquedas
  │   ├─ sales.py            # vender/devolver entradas
  │   ├─ report.py           # reporte on-demand
  │   └─ logging_conf.py     # logger a app.log
  ├─ docs/
  │   └─ manual_tests.md     # pruebas manuales sugeridas
  ├─ .gitignore
  ├─ README.md
  └─ data.json               # (opcional; se genera al guardar y salir)
```