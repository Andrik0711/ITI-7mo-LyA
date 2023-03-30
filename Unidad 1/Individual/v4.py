import json

"Desarrollado por: JOSE ANDRIK MARTINEZ RODRIGUEZ, 2030152"


# Cargar el archivo JSON
with open('ejemplo.json', 'r') as f:
    data = json.load(f)

# Crear un diccionario para representar el grafo
grafo = {}

# Iterar a través de cada par de nodos y su peso
for key, value in data['el'].items():
    nodo1 = str(value['u'])
    nodo2 = str(value['v'])
    peso = str(value['w'])

    # Agregar los nodos al diccionario si aún no existen
    if nodo1 not in grafo:
        grafo[nodo1] = {}
    if nodo2 not in grafo:
        grafo[nodo2] = {}

    # Agregar las aristas a los nodos
    grafo[nodo1][nodo2] = peso
    grafo[nodo2][nodo1] = peso

# Imprimir el diccionario como una representación de grafo
print("Representacion de un GRAFO:")
print("g = {")
for nodo, aristas in grafo.items():
    aristas_str = ", ".join(
        [f'"{nodo2}": {peso}' for nodo2, peso in aristas.items()])
    print(f'"{nodo}" : {{ {aristas_str} }},')
print("}")
