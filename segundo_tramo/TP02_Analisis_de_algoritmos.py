# -*- coding: utf-8 -*-

# Guía Práctica N° 2: Análisis de Algoritmos ⌛




---

## Objetivos
----

-   Definir qué es un algoritmo y comprender su importancia en la resolución de problemas.
-   Conocer la diferencia entre algoritmos iterativos y recursivos clásicos.
-   Reflexionar sobre elementos del análisis de algoritmos y su impacto en el tiempo de ejecución.
-   Construir algoritmos de búsqueda y ordenamiento para la organización de listas de datos.
-   Aplicar algoritmos de regresión y clustering de *sklearn* en el contexto de la ciencia de datos.

# Ejercicios ✍ 🤓

1) Factorial Recursivo: Escribe un programa en Python que calcule el factorial de un número entero utilizando una función recursiva. ¿Cuántas llamadas recursivas se realizan?
"""

# Resolución 1)

def factorial_rec(nn):
  if nn == 0: # caso base / trivial
    return 1
  else:
    return nn * factorial_rec(nn - 1)

n = 10
factorial = factorial_rec(n)
print(f'El resultado del factorial {n} es igual a {factorial}')

# La función realiza N llamadas recursivas, hasta llegar al valor nn == 0, momento en el cual se alzanca el caso base.

"""2) Escribir una función `buscar_ultimo_elemento()`que reciba una lista y un elemento y devuelva la posición de la última aparición de ese elemento en la lista o `-1` si el elemento no está en la lista."""

# Resolución 2)

def buscar_ultimo_elemento(lista,elemento):
  indice = -1
  for i,e in enumerate(lista):
    if e == elemento:
      indice = i
  return indice

lista_ej_2 = [1,2,3,4,5,5,5,7,7]

print(buscar_ultimo_elemento(lista_ej_2,5))
print(buscar_ultimo_elemento(lista_ej_2,8))

"""3) Escribir una función `buscar_n_elemento()` que reciba una lista y un elemento y devuelva la cantidad de veces que aparece el elemento en la lista o `-1` si el elemento no está en la lista."""

# Resolución 3)

def buscar_n_elemento(lista,elemento):
  resultado = -1
  existe = False

  for e in lista:
    if e == elemento:
      resultado += 1
      existe = True

  if existe == True:
    resultado += 1

  return resultado

print(buscar_n_elemento(lista_ej_2,7))
print(buscar_n_elemento(lista_ej_2,5))

"""4) Escribir una función `maximo()` que busque el valor máximo de una lista de números positivos. Python tiene la función integrada `max()`pero como práctica te proponemos que realices la implementación sin usarla."""

# Resolución 4)

def maximo(lista):
  min = lista[0]
  for e in lista:
    if e < min:
      min = e

  max = min
  for e in lista:
    if e > max:
      max = e

  print('El valor máximo de la lista proporcionada es:',max)

lista_NN = [4,4,3,2,9,2,7,2,2]
maximo(lista_NN)

"""5) Búsqueda Binaria: Implementa el algoritmo de búsqueda binaria en su versión recursiva. Dado un número objetivo y una lista ordenada de números, el programa debe determinar si el número objetivo está presente en la lista."""

# Resolución 5)

def busqueda_binaria_rec(listaOrdenada, objetivo, Lizq = 0, Lder = None):

    izq = Lizq

    if Lder == None:
      der = len(listaOrdenada)-1
    else:
      der = Lder

    medio = (izq + der)//2

    if izq <= der:
      if listaOrdenada[medio] == objetivo:
        return medio
      elif listaOrdenada[medio] < objetivo:
        izq = medio + 1
        return busqueda_binaria_rec(listaOrdenada, objetivo, izq, der)
      else:
        der = medio - 1
        return busqueda_binaria_rec(listaOrdenada, objetivo, izq, der)
    return -1

def busqueda_binaria_comp(listaordenada, objetivo):
  resultado = busqueda_binaria_rec(listaordenada,objetivo)
  if resultado != -1:
    print('El elemento está en la lista, en la posición',resultado)
  else:
    print('El elemento no está en la lista.')

lista_ej_5 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
busqueda_binaria_comp(lista_ej_5,17)

"""6) Ordenamiento de Selección: Escribe una función que realice el ordenamiento de selección en una lista de números enteros."""

# Resolución 6)

def ordenamientoPorSeleccion(unaLista):
   for llenarRanura in range(len(unaLista)-1,0,-1):
       posicionDelMayor=0
       for ubicacion in range(1, llenarRanura+1):
           if unaLista[ubicacion]>unaLista[posicionDelMayor]:
               posicionDelMayor = ubicacion

       temp = unaLista[llenarRanura]
       unaLista[llenarRanura] = unaLista[posicionDelMayor]
       unaLista[posicionDelMayor] = temp

   return unaLista

import numpy as np

def lista_random(nn):                              # Función para crear lista de números naturales aleatorios del 1 al 100, según la cantidad de elementos
  lista_rand = list((np.random.rand(nn)*100))      # pasada por parámetro.

  for i,n in enumerate(lista_rand):
    lista_rand[i] = round(n)

  return lista_rand

lista_8NN = lista_random(8)
print(lista_8NN)

ordenamientoPorSeleccion(lista_random(20))

"""7) Tiempo de Ejecución: Calcula y compara el tiempo de ejecución de los algoritmos de búsqueda lineal y búsqueda binaria en diferentes tamaños de listas."""

# Resolución 7)

# En este ejercicio se compara la versión de busqueda binaria recursiva (ej. 5) y la busqueda lineal iterativa en una lista ordenada, definida a continuación.


def busqueda_lineal_ordenado(lista, item):
    pos = -1
    for i, elemento in enumerate(lista):
        if elemento == item:
            pos = i
            break
        elif elemento > item:
            break
    return pos

# Se crean varias listas de distinto tamaño (ordenadas):

listaej7_1 = list(range(1001))
listaej7_2 = list(range(5001))
listaej7_3 = list(range(10001))

# Commented out IPython magic to ensure Python compatibility.
# Se mide tiempo de ambos métodos de búsqueda:
import time

print('-Tiempos de ejecución en lista de 1000 elementos-')
print('Búsqueda lineal:')
# %time busqueda_lineal_ordenado(listaej7_1,500)
print('Búsqueda binaria recursiva:')
# %time busqueda_binaria_rec(listaej7_1,500)
print('\n')
print('-Tiempos de ejecución en lista de 5000 elementos-')
print('Búsqueda lineal:')
# %time busqueda_lineal_ordenado(listaej7_2,3500)
print('Búsqueda binaria recursiva:')
# %time busqueda_binaria_rec(listaej7_2,3500)
print('\n')
print('-Tiempos de ejecución en lista de 10000 elementos-')
print('Búsqueda lineal:')
# %time busqueda_lineal_ordenado(listaej7_3,7000)
print('Búsqueda binaria recursiva:')
# %time busqueda_binaria_rec(listaej7_3,7000)
print()

# Del análisis de los valores obtenidos se deduce que la búsqueda binaria es más rápida en todos los casos. Observamos que:

# Para una lista de 1000 elementos, la búsqueda binaria tomó apenas un 9.4% con respecto al tiempo de la búsqueda lineal.
# En el caso de la lista de 5000 elementos, la búsqueda binaria tomó un 3.6% con respecto al tiempo de la búsqueda lineal.
# Por último, en una lista de 10000 elementos,  la búsqueda binaria tomó un 1.95% con respecto al tiempo de la búsqueda lineal.

# Se concluye entonces que a mayor cantidad de elementos, más notable es la diferencia entre el tiempo de ejecución de una y otra función,
# para una lista con los mismos elementos.

"""8) Regresión Lineal: Utiliza la biblioteca scikit-learn para ajustar un modelo de regresión lineal a un conjunto de datos de tu elección. Muestra el gráfico de dispersión de los datos reales y las predicciones del modelo."""

# Resolución 8) Para este ejercicio se utilizó el CSV 'redes_sociales'

from google.colab import drive

drive.mount('/content/drive')

"""Link al archivo utilizado:
https://drive.google.com/file/d/1YB_DuRsfaSo5wLRhGgQgDsGsFeE-b-nc/view?usp=drive_link
"""

import pandas as pd

redes_sociales_reg = pd.read_csv('/content/drive/MyDrive/Archivos auxiliares Curso Python/redes_sociales.csv') #Editar

display(redes_sociales_reg)

# Ahora se define la X y la Y que evaluaremos en el modelo. En este caso X será número de publicaciones, e Y cantidad de seguidores.

X = redes_sociales_reg.iloc[:, 2:3]
y = redes_sociales_reg.iloc[:, 1:2]

#Se muestra el gráfico de dispersión de los datos

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(8,5))
plt.scatter(X, y, s=30, c='b', marker='x')
plt.xlabel('Cantidad de publicaciones en perfil')
plt.ylabel('Cantidad de seguidores');
plt.grid(True)

# Se crea objeto LinearRegression y se le entrena

from sklearn.linear_model import LinearRegression

pubs_seguidores = LinearRegression()
pubs_seguidores.fit(X, y)

# Ya una vez que el modelo está entrenado, graficamos tanto la dispersión como la predicción.

plt.figure(figsize=(8,5))
plt.scatter(X, y, s=30, c='b', marker='x', label='Valores objetivo')
plt.plot(X, pubs_seguidores.predict(X), color='g', lw=1, label='Predicción')
plt.xlabel('Cant. de publicaciones en perfil')
plt.ylabel('Cant. de seguidores');
plt.legend(loc=9)
plt.grid(True)

# Cálculo MSE:

from sklearn.metrics import mean_squared_error

y_pred = pubs_seguidores.predict(X)
mean_squared_error(y, y_pred)

# se observa que el MSE es bastante alto, a pesar de que el modelo posee buen r2_score (siguiente).

# Por último, se calcula el R2_score para probar el modelo:

from sklearn.metrics import r2_score

y_pred = pubs_seguidores.predict(X)
r2_score(y, y_pred)

# Se concluye que la predicción es satisfactoria, ya que el R cuadrado está muy cerca de 1.

"""9) Algoritmo K-Means: El algoritmo K-Means se encuentra disponible en la biblioteca scikit-learn. Aplica el algoritmo a un conjunto de datos y muestra los grupos resultantes en un gráfico.

Link al archivo utilizado:
https://drive.google.com/file/d/1pMGvsq3namRf3jSvot1SuhkarBWzfeuX/view?usp=drive_link
"""

# Resolución 9)

# Se empleó para esta solución la tabla bikeshare_stations, de la BD bikeshare.

import pandas as pd
from sqlalchemy import create_engine, text, inspect

url = "sqlite:////content/drive/MyDrive/Curso Python Colab/Primer tramo/bikeshare.db" #Editar según ruta actual
bikeshare = create_engine(url)

def pasar_a_DF(consulta):                                # Función para automatizar el pasaje de información de la base a un Dataframe.
    with bikeshare.connect() as conexion:
        df = pd.read_sql(text(consulta), conexion)
    return df

consulta_1 = 'SELECT latitude, longitude FROM bikeshare_stations'

ubicacion_estaciones = pasar_a_DF(consulta_1)     # Se crea DF que contiene las columnas de latitud y longitud.

display(ubicacion_estaciones)

# Se crean las variables a utilizar a partir del DF creado anteriormente

X = ubicacion_estaciones.iloc[:, 0:1]
y = ubicacion_estaciones.iloc[:, 1:]

import matplotlib.pyplot as plt

plt.scatter(X, y, c='white', marker='o', edgecolor='black', s=30)
plt.xlabel('Latitud')
plt.ylabel('Longitud')

plt.grid(True)
plt.tight_layout()
plt.show()

# Se observa un punto muy alejado del resto de las estaciones, y se procede a eliminarlo, ya que es un valor que no aplica para el estudio.

consulta_2 = 'SELECT latitude, longitude FROM bikeshare_stations WHERE longitude < -76.'

ubicacion_estaciones = pasar_a_DF(consulta_2)     # Se crea DF que contiene las columnas de latitud y longitud.

# Se reasignan las variables según el DF ajustado.

X = ubicacion_estaciones.iloc[:, 0:1]
y = ubicacion_estaciones.iloc[:, 1:]

import matplotlib.pyplot as plt

plt.scatter(X, y, c='white', marker='o', edgecolor='black', s=30)
plt.xlabel('Latitud')
plt.ylabel('Longitud')

plt.grid(True)
plt.tight_layout()
plt.show()

# Ahora se observa una distribución satisfactoria para aplicar el clustering.

X2 = ubicacion_estaciones.iloc[:, 0:2] # Se prepara la variable para contener ambas columnas del DF.

from sklearn.cluster import KMeans

# Se calcula el número óptimo de clusters

inercias=[]
for i in range(1,10):
    kmeans = KMeans(n_clusters=i, n_init=20, random_state=0)
    kmeans.fit(X2)
    inercias.append(kmeans.inertia_)

plt.plot(range(1,10),inercias)
plt.title('Método del codo (The Elbow Method)')
plt.xlabel('Número de clusters')
plt.ylabel('Inercia')
plt.show()

# Según el gráfico anterior, no se observan codos muy marcados. Se tomarán 5 clusters para este análisis.

km = KMeans(n_clusters=9, n_init=60, random_state=0)

y_km = km.fit_predict(X2)

y_km   # Grupos resultantes

km.cluster_centers_

centrosX = km.cluster_centers_[:,0:1]
centrosY = km.cluster_centers_[:,1:]

# Gráfico superponiendo el scatter de los pares originales y los centroides.

plt.scatter(X, y, c='white', marker='o', edgecolor='black', s=30)
plt.scatter(centrosX, centrosY, c='red', marker='o', edgecolor='black', s=30)
plt.xlabel('Latitud')
plt.ylabel('Longitud')
plt.grid(True)
plt.tight_layout()
plt.show()
