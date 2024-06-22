# -*- coding: utf-8 -*-

# Guía Práctica N° 3: Grafos aplicados a ciencia de datos




---

## Objetivos
----

* Aprender qué son los grafos, sus clasificaciones y cómo pueden emplearse para plantear la solución a problemas de ciencia de datos.
* Aplicar algoritmos de búsqueda de caminos óptimos con la ayuda de grafos.
* Encontrar componentes fuertemente conexas en colecciones de datos.
* Conocer algoritmos de optimización de redes para encontrar árboles de expansión de costo mínimo.
* Aplicar herramientas para manejar y visualizar grafos.

# Ejercicios y Problemas ✍ 🤓
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import networkx as nx
import seaborn as sns

"""## 1) Ejercicio de práctica
Generar un grafo dirigido de 5 nodos que responden al siguiente comportamiento:

'Lautaro' y 'Melisa' siguen a 'Alejandro', 'Marina' y 'Gimena'.

 'Marina' sigue a 'Melisa', 'Lautaro' y 'Alejandro'.

 'Alejandro' y 'Gimena' se siguen mutuamente.


Gráficar de modo circular y verificar las correspondencias.

"""

# Solución Ej. 1)

grafo_1 = nx.DiGraph()

grafo_1.add_node('Melisa')
grafo_1.add_node('Alejandro')
grafo_1.add_node('Caupo')
grafo_1.add_node('Marina')
grafo_1.add_node('Gimena')

docentes = ['Caupo','Melisa']
alumnos = ['Alejandro','Marina','Gimena']

for doc in docentes:
  for al in alumnos:
    grafo_1.add_edge(doc, al)
  grafo_1.add_edge('Marina', doc)

grafo_1.add_edge('Alejandro','Gimena')
grafo_1.add_edge('Gimena','Alejandro')
grafo_1.add_edge('Marina','Alejandro')

colors = sns.color_palette('pastel', 5)
sns.set_palette(colors)

plt.figure(figsize=(4,4))
nx.draw_circular(grafo_1,
                 node_color='C4',
                 node_size=1500,
                 with_labels=True,
                 edge_color='k'
                 )
plt.show()

"""## 2) Ejercicio de práctica (Para aplicar BEA)
En el archivo [Graph1.txt](https://drive.google.com/file/d/1TlMQhcS5BHWbJLdAu4VAIlTYUPuTzZoa/view?usp=sharing) se tiene un listado con los nombres de nodos de un grafo, se tiene un par de nodos por línea representando las aristas. Lea el archivo y cree una lista de tuplas para usar con la función add_edges_from() para crear un grafo no dirigido.

Aplique la BEA Al grafo obtenido iniciando desde el nodo go y grafique los distintos niveles.
"""

# Solución Ej. 2)

from networkx.drawing.nx_pylab import circular_layout
from google.colab import files, drive
drive.mount('/content/drive')

txt_ej2 = "/content/drive/MyDrive/Curso Python Colab/Segundo tramo/Graph1.txt"   # Editar según ubicación de archivo txt.

with open(txt_ej2, 'r') as archivo:         # Apertura del archivo previante cargado y recorrido de sus líneas.
  datos_ej2 = archivo.readlines()

tuplas_ej2 = []
dicc_ej2 ={}

for linea in datos_ej2:                       # Código para generar la lista de tuplas a partir del archivo txt. A modo de práctica,
  origen, destino = linea.strip().split()
  tuplas_ej2.append((origen, destino))
  if origen not in dicc_ej2.keys():           # A modo de prueba, se agregó este condicional para crear un diccionario.
    dicc_ej2[origen] = [destino]
  else:
    dicc_ej2[origen].append(destino)

tuplas_ej2

dicc_ej2

grafo_ej2 = nx.Graph()                         #Se crea grafo no dirigido y se grafica.
grafo_ej2.add_edges_from(tuplas_ej2)

plt.figure(figsize=(4,4))
nx.draw_circular(grafo_ej2,
                 node_color='C0',
                 node_size=500,
                 with_labels=True,
                 edge_color='k'
                 )
plt.show()

predecesores_ej2 = nx.bfs_predecessors(grafo_ej2, source='go')
lista_pred_ej2 = list(predecesores_ej2)
lista_pred_ej2

def detectar_niveles_bea(lista_predecesores):  # Función sencilla para analizar una lista de predecesores y detectar la cantidad de niveles.

    niveles = 1
    lista_d = []

    for par in lista_predecesores:   # Se crea lista con todos los predecesores.
      lista_d.append(par[1])

    set_d = set(lista_d)  # Se crea un set a partir de la lista, para eliminar los duplicados.

    for e in set_d:
      if lista_d.count(e) > 1:
        niveles += 1

    return print(f'{niveles} niveles detectados.')

detectar_niveles_bea(lista_pred_ej2)

nodes_pos_ej2 = nx.circular_layout(grafo_ej2)      # Creación de objeto conteniendo posiciones, y gráfico de niveles a continuación.

bea0 = nx.bfs_tree(grafo_ej2, source='go', depth_limit=0)   # depth_limit=0 para graficar con otro color el nodo de partida.
bea1 = nx.bfs_tree(grafo_ej2, source='go', depth_limit=1)
bea2 = nx.bfs_tree(grafo_ej2, source='go', depth_limit=2)
bea3 = nx.bfs_tree(grafo_ej2, source='go', depth_limit=3)

plt.figure(figsize=(4,4))
nx.draw_circular(grafo_ej2, edge_color='lightgray')                # Se grafican las aristas no utilizadas por el algoritmo de búsqueda en color gris.
nx.draw(bea3, nodes_pos_ej2, with_labels=True, node_color="C3", edge_color="orange")   # i, h
nx.draw(bea2, nodes_pos_ej2, with_labels=True, node_color="C1", edge_color="blue")  # d, e, f, g
nx.draw(bea1, nodes_pos_ej2, with_labels=True, node_color="C0", edge_color="green") # a, b, c
nx.draw(bea0, nodes_pos_ej2, with_labels=True, node_color="C2")  # go
plt.show()

"""## 3) Ejercicio de práctica (Para aplicar BEP)

En el archivo [Graph2.txt](https://drive.google.com/file/d/1iaWPYLwN-gDkbon69RG-ZlttiVwTxEVV/view?usp=sharing) se tiene un listado con los nombres de nodos de un grafo, se tiene un par de nodos por línea representando las aristas. Lea el archivo para crear un **grafo dirigido**.

Aplique la **BEP** Al grafo obtenido iniciando desde el nodo `0` y grafique el resultado.
"""

# Solución Ej. 3)

txt_ej3 = "/content/drive/MyDrive/Curso Python Colab/Segundo tramo/Graph2.txt"

with open(txt_ej3, 'r') as archivo:
  datos_ej3 = archivo.readlines()
                                         #
tuplas_ej3 = []                          # Generación de lista de tuplas a partir del archivo txt.
                                         #
for linea in datos_ej3:
  origen, destino = linea.strip().split()
  tuplas_ej3.append((origen, destino))

grafo_ej3 = nx.DiGraph(tuplas_ej3)                         #Se crea grafo dirigido y se grafica.

plt.figure(figsize=(12,4))
nx.draw_planar(grafo_ej3,
                 node_color='C2',
                 node_size=200,
                 with_labels=True,
                 edge_color='k'
                 )
plt.show()

bep_ej3 = nx.dfs_tree(grafo_ej3, source='0')
list(bep_ej3)

# Se grafica el resultado del análisis. Los nodos y aristas en color gris representan aquellos/as que no fueron
# visitados/utilizadas por el algoritmo.

nodes_pos_ej3 = nx.planar_layout(grafo_ej3)

plt.figure(figsize=(12,4))
nx.draw_planar(grafo_ej3,
                 node_color='lightgray',
                 node_size=200,
                 with_labels=True,
                 edge_color='lightgray'
                 )
nx.draw(bep_ej3, nodes_pos_ej3,  node_size=200, with_labels=True, node_color="C2", edge_color="darkblue")
plt.show()

# Se osberva que el análisis BEP no busca el camino más corto, sino que explora los caminos posibles desde el punto de partida indicado
# respetando el orden de la información en el archivo original de adyacencias.

"""### 4) Ejercicio de práctica (Para aplicar CFC)

Escribir el código necesario para graficar el siguiente grafo con _NetworkX_:

<center><img src="https://drive.google.com/uc?export=view&id=1p0X6ZujB8tPy-FhWWzVCSn2ElwO8EPOV" width=450 alt="centered image"></center>

Una vez creado, encuentre sus **CFC**.

"""

# Solución Ej. 4)

# Primero se crea el diccionario de adyacencias, luego se crea objeto de grafo y posteriormente se definen las posiciones de los nodos,
# tomando como punto de origen (0,0) el nodo '8'. Finalmente se grafica el resultado.

dicc_ej4 = {'0':['1','5'],'1':['2','3','8'],'2':['0'],'3':['2','4','7'],'4':['6'],'5':['4'],'6':['5'],'7':['8','10','12'],'8':['11'],'9':['7'],'10':['11','14'],'11':['9','15'],'12':['13'],'13':['15'],'14':['12'],'15':['14']}

digrafo_ej4 = nx.DiGraph(dicc_ej4)

long_lat_ej4 = {
    '0':(1,4),
    '1':(0,3),
    '2':(2,3),
    '3':(1,2),
    '4':(3,2),
    '5':(3,4),
    '6':(4,3),
    '7':(1,1),
    '8':(0,0),
    '9':(1,0),
    '10':(2,0),
    '11':(1,-1),
    '12':(3,1),
    '13':(4,1),
    '14':(3,0),
    '15':(4,-1)
}

plt.figure(figsize=(6,4))
nx.draw(
    digrafo_ej4,
    pos=long_lat_ej4,
    node_color='C1',
    node_shape='o',
    node_size=500,
    font_size=10,
    with_labels=True,
)
plt.show()

# Se aplica el método requerido en la consigna:
cfc = list(nx.strongly_connected_components(digrafo_ej4))
print("Componentes Fuertemente Conectados:")
print(cfc)
