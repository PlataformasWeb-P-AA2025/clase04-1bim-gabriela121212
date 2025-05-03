import requests
import json

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    lista_datos.append(d)

base_datos = "personas005"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}


# Enviar datos
for i,doc in enumerate(lista_datos, start=1):
    response = requests.post(url,json=doc)
    print(f"Insertando objeto {i} | {response.status_code}")
