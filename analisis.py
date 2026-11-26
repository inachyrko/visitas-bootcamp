"""KPI de ejemplo para las prácticas de Git y GitHub.

Solo usa módulos de la librería estándar de Python.
"""

import csv
from pathlib import Path


ruta = Path(__file__).parent / "datos" / "visitas.csv"

with ruta.open(encoding="utf-8", newline="") as archivo:
    registros = list(csv.DictReader(archivo))

visitas = len(registros)
conversiones = 0

for registro in registros:
    if registro["conversion"] == "1":
        conversiones += 1

tasa = conversiones / visitas * 100 if visitas else 0

print("=== Informe de visitas ===")
print(f"Visitas: {visitas}")
print(f"Conversiones: {conversiones}")
print(f"Tasa de conversion: {tasa:.1f}%")
