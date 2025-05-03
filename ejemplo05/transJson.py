import csv
import json

archivo_csv = 'atp_tennis.csv'
archivo_json = 'datos.json'

columnas = [
    "Tournament", "Date", "Series", "Court", "Surface", "Round", "Best of",
    "Player_1", "Player_2", "Winner", "Rank_1", "Rank_2", "Pts_1", "Pts_2",
    "Odd_1", "Odd_2", "score"
]

datos = {"docs": []}

# Leer CSV
with open(archivo_csv, mode='r', encoding='latin1') as a_csv:
    lector = csv.reader(a_csv)
    next(lector) 
    for fila in lector:
        if len(fila) < len(columnas):
            continue
        fila_dict = {col: fila[i] for i, col in enumerate(columnas)}
        datos["docs"].append(fila_dict)

# Guardar como JSON
with open(archivo_json, mode='w', encoding='utf-8') as archivo_salida:
    json.dump(datos, archivo_salida, indent=4, ensure_ascii=False)

print(f"Proceso completo: {len(datos['docs'])} registros.")
