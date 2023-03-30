# ejemplo de un archivo json sacado de visual algo
""" 
Para cuando todos estan seguidos 1-6
{"vl":{"0":{"x":140,"y":40},"1":{"x":240,"y":20},"2":{"x":320,"y":60},"3":{"x":420,"y":60},"4":{"x":280,"y":160},"5":{"x":380,"y":160},"6":{"x":500,"y":160}},
"el":{"0":{"u":0,"v":1,"w":1},"1":{"u":1,"v":2,"w":1},"2":{"u":2,"v":3,"w":1},"3":{"u":3,"v":4,"w":1},"4":{"u":4,"v":5,"w":1},"5":{"u":5,"v":6,"w":1}}}

Para cuando uno de los nodos es bidireccional
{"vl":{"0":{"x":200,"y":60},"1":{"x":280,"y":60},"2":{"x":380,"y":60},"3":{"x":460,"y":60},"4":{"x":540,"y":60},"5":{"x":620,"y":60},"6":{"x":700,"y":40}},
"el":{"0":{"u":0,"v":1,"w":1},"1":{"u":1,"v":2,"w":1},"2":{"u":2,"v":3,"w":1},"3":{"u":3,"v":4,"w":1},"4":{"u":4,"v":5,"w":1},"5":{"u":5,"v":6,"w":1},"6":{"v":0,"u":1,"w":1}}}

"el":{"0":{"u":0,"v":1,"w":1},"1":{"u":1,"v":2,"w":1},"2":{"u":2,"v":3,"w":1},"3":{"u":3,"v":4,"w":1},"4":{"u":4,"v":5,"w":1},"5":{"u":5,"v":6,"w":1}}}
"el":{"0":{"u":0,"v":1,"w":1},"1":{"u":1,"v":2,"w":1},"2":{"u":2,"v":3,"w":1},"3":{"u":3,"v":4,"w":1},"4":{"u":4,"v":5,"w":1},"5":{"u":5,"v":6,"w":1},"6":{"v":0,"u":1,"w":1}}}
"""
import json

# some JSON:
x = (input(": "))

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# load_archive = []
# load_archive = input("ingrese el archivo json: ")

# iteramos nuestro arreglo
# for longitud in range(len(load_archive)):
#     print(load_archive[longitud])


# tratar de encontrar algun valor en el array recibido
# x = json.loads(load_archive)
# print(x["v"])
