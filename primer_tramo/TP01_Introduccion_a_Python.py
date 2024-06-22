# -*- coding: utf-8 -*-

# Guía Práctica N° 1: Introducción a Python 🐍




---

Los siguientes ejercicios implican el uso de los conceptos teóricos incluidos en los módulos I del curso.
Para la realización de la guía se sugiere tener a mano el material desarrollado en clase.
Es importante que los ejercicios se resuelvan y entreguen de manera organizada, documentando e imprimiendo los resultados correspondientes para cada uno.

## Objetivos
----

- Comprender la estructura básica de un programa en Python: Aprender la sintaxis y las reglas básicas incluyendo la identificación de palabras reservadas y la estructura de bloques de código.

- Aprender sobre los diferentes tipos de datos disponibles en Python, como enteros, flotantes, cadenas, listas y diccionarios, y comprender sus características y usos.

- Aprender a utilizar las estructuras de control, como condicionales (if - else), bucles (for, while) y estructuras de control anidadas para controlar el flujo de ejecución de un programa.

- Manejar flujos de entrada y salida: interactuar con el usuario mediante la entrada de datos desde el teclado y la salida de resultados a través de la consola.

- Interpretar y depurar errores: identificar y solucionar errores comunes en Python, utilizando técnicas de depuración y herramientas de manejo de excepciones.

- Comprender el concepto de funciones en Python y aprender a definir y llamar funciones para modularizar y reutilizar el código.

- Aprender a dividir un programa en módulos más pequeños y organizados para facilitar su desarrollo y mantenimiento. Entender cómo importar módulos y paquetes estándar en Python.

- Explorar las funciones predefinidas y la manipulación de archivos: utilizar las funciones predefinidas en los módulos y paquetes estándar de Python, y aprender a manipular archivos, como leer y escribir datos en diferentes formatos.

# Ejercicios ✍ 🤓

1) Escribir un programa que pida al usuario ingresar el lado de un cuadrado y devuelva su perímetro y su área correspondiente.
"""

# Resolución Ej. 1:

print('-Cálculo del perímetro y área de un cuadrado-\n')

lado = float(input('Ingrese la longitud del lado de un cuadrado en cm: ')) # Se solicita al usuario ingresar el dato requerido.

print(f'\nEl perímetro de un cuadrado de {lado} cm de lado es de {lado*4} cm, y su área es de {lado**2} cm².') # Se calculan e imprimen los resultados.

"""2) Escribir un programa que pida al usuario ingresar el radio de un círculo y devuelva su área (en este caso, debe validar el dato ingresado por el usuario)."""

# Resolución Ej. 2:

print('-Cálculo del área de un círculo-\n')

import math

'''La siguiente función solicita al usuario ingresar el radio, y valida si es numérico y positivo.
Si se cumplen ambas condiciones, realiza el cálculo y presenta el resultado.
En caso contrario, informa al usuario del error y solicita un nuevo radio.'''

def validacion():
    radio = input()
    if radio.isdigit():
      if float(radio) > 0:
        print(f'\nEl área de un círculo de {radio} cm de radio es de {round(math.pi * math.pow(float(radio),2),2)} cm²')
      else:
        print('\nEl radio ingresado debe ser positivo. Por favor, ingrese un radio válido:')
        validacion()
    else:
      print('\nEl valor ingresado debe ser un número. Por favor ingrese un valor numérico:')
      validacion()

print('Ingrese la longitud del radio de un círculo en cm:') # Mensaje fuera de la función, para que sea reemplazado por el de excepción, de ser necesario.
validacion()

"""3) Escribir un programa que permita ingresar al usuario una cadena de caracteres y determine mediante una función, definida por usted, la cantidad de vocales que posee."""

# Resolución Ej. 3:

print('-Conteo de vocales-\n')

'''La función recorre la cadena de caracteres ingresada por el usuario.
Si el caracter analizado en el ciclo FOR se encuentra dentro de la lista de vocales declarada,
suma una unidad al contador, y finalmente presenta el resultado.'''

def cantidad_vocales():
    vocales = ['a','e','i','o','u','á','é','í','ó','ú']
    contador = 0
    cadena = input('Ingrese una cadena de caracteres: ').strip()

    for letra in cadena:
      if letra.lower() in(vocales):    # Si la cadena tiene caracteres en mayúscula, la función lower() los cambiará a minúscula y permitirá su correcta comparación con la lista de vocales, que está en minúscula.
        contador += 1

    print(f'\nLa cadena de caracteres que ingresó contiene {contador} vocales.') # Se presenta el resultado.

cantidad_vocales()

"""4) Escribir un programa que pida al usuario dos palabras y determine si las mismas riman o no. Considere que las dos palabras riman si coinciden en sus tres últimas letras."""

# Resolución Ej. 4:

print('-Palabras que riman-\n')

def riman():
    cadena = input().strip() # Solicita al usuario ingresar texto y elimina espacios al principio y final de la cadena. Se declaran las variables.
    cantidad_espacios = 0
    palabra1 = ''
    palabra2 = ''

    for caracter in cadena:    # Se cuenta la cantidad de espacios entremedio de las palabras, y en caso de ser mayor o menor 1,
      if caracter ==' ':       # se muestra el mensaje de error correspondiente.
        cantidad_espacios += 1

    if cantidad_espacios > 1:
      print('\nUsted ha ingresado más de dos palabras, o más de dos espacios de separación.\nPor favor, ingrese dos palabras separadas por un espacio:')
      riman()
    elif cantidad_espacios < 1:
      print('\nUsted ha ingresado una o ninguna palabra.\nPor favor, ingrese dos palabras separadas por un espacio:')
      riman()
    else:
      palabra1, palabra2 = cadena.split()  # Si el usuario ingresa exactamente dos palabras separadas por espacios,
                                           # se procede a determinar si las palabras riman de acuerdo al criterio provisto.
      if palabra1.lower()[-3:] == palabra2.lower()[-3:]:
        print(f"\nLas palabras ingresadas riman, ya que ambas terminan con '{palabra1[-3:]}'.")
      else:
        print(f"\nLas palabras ingresadas no riman, ya que la primera termina con '{palabra1[-3:]}' y la segunda con '{palabra2[-3:]}'.")

print('Ingrese dos palabras separadas por un espacio:') # Mensaje fuera de la función, para que sea reemplazado por el de excepción, de ser necesario.

riman()

"""5) Escribir un programa que permita al usuario ingresar una lista con notas de exámenes. El programa debe devolver por consola el promedio de notas y el porcentaje de alumnos que aprobaron y desaprobaron. (Se considera aprobado con una nota mayor o igual a 60%).

Aclaración: no utilice funciones incluidas como por ejemplo la función len().
"""

# Resolución Ej. 5:

print('-Análisis de notas-\n')

print('Ingrese los apellidos de los alumnos y las notas que obtuvieron, separada por un espacio.\nUtilice coma (,) para separar cada registro. (Ej: Álvarez 70, Torres 80, ...)')

string_notas = input()  # El usuario ingresa las notas en una sola cadena, según las instrucciones.

'''A continuación, se divide por primera vez la cadena y se crea una lista en donde cada ítem es el alumno y su respectiva nota,
y se declaran las variables necesarias'''

lista_AyN = list(string_notas.strip().split(','))
dic_AyN = {}
q_alumnos = 0
q_aprobados = 0
sumatoria_notas = 0

'''El ciclo FOR recorre los ítems de la lista anteriormente generada, y los vuelve a separar, organizando
los elementos obtenidos en un diccionario. A su vez se aprovecha el ciclo para determinar cantidad de alumnos,
cantidad de aprobados, y sumatoria de notas; información que luego es utilizada para calcular y presentar
los resultados.'''

for registro in lista_AyN:
    alumno, nota = registro.strip().split()
    nota = float(nota)
    dic_AyN[alumno] = nota
    q_alumnos += 1
    sumatoria_notas += nota
    if nota >= 60:
      q_aprobados += 1

q_desaprobados = q_alumnos - q_aprobados

input('\nLos registros fueron ingresados. Presione Enter para continuar... ')

print(f'\nEl promedio de notas fue de {round(sumatoria_notas/q_alumnos,2)}.')
print(f'Porcentaje de aprobados: {round((q_aprobados/q_alumnos)*100,2)}%')
print(f'Porcentaje de desaprobados: {round((q_desaprobados/q_alumnos)*100,2)}%')

"""6) Escribir un programa que solicite al usuario ingresar una lista de alturas en centímetros. El programa debe calcular y mostrar por pantalla el promedio de alturas y el porcentaje de alturas que están por encima de la media."""

# Resolución Ej. 6:

print('-Trabajo con alturas-\n')

cadena_alturas = input('Ingrese las alturas en cm que desea incluir en el análisis, separando cada valor con un espacio: ')

# Se genera una lista a partir de la cadena ingresada, convirtiendo en el proceso los elementos de str a float, mediante comprensión de listas:
lista_alturas = [float(altura) for altura in list(cadena_alturas.strip().split())]

#Se realizan los calculos pertinentes, y se presentan los resultados:
promedio_alturas = round(sum(lista_alturas) / len(lista_alturas),2)
alturas_mayores = 0

for altura in lista_alturas:
    if altura > promedio_alturas:
      alturas_mayores += 1

print(f'\nEl promedio de las alturas ingresadas es de {promedio_alturas}, y el porcentaje de alturas que superan dicho valor es de {(alturas_mayores/len(lista_alturas))*100}%.')

"""7) Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros) y mediante una función, definida por usted, calcule el índice de masa corporal y lo almacene en una variable. El programa debe mostrar por pantalla la frase “Tu índice de masa corporal es <imc>”, donde <imc> es el índice de masa corporal calculado (redondee el valor a dos decimales)."""

# Resolución Ej. 7:

print('-Cálculo de Índice de Masa Corporal (IMC)-\n')

peso_kg = float(input('Ingresa tu peso en Kg: '))
estatura_m = float(input('Ingresa tu estatura en metros: '))

def calcular_IMC(peso, estatura):
    IMC = peso / (estatura**2)
    return IMC

IMC = calcular_IMC(peso_kg, estatura_m)

print(f'Tu índice de masa corporal es {round(IMC,2)}')

"""8) Escribir un programa que permita almacenar nombres y edades en un diccionario y a partir del mismo calcule la cantidad de personas mayores de 25. (Utilice la biblioteca NumPy)."""

# Resolución Ej. 8:

print('-Trabajo con edades-\n')

import numpy as np

''' La siguiente función pide al usuario que ingrese un nombre y la edad de la persona, para ser agregado el registro al diccionario.
Al final se pregunta al usuario si desea cargar otro registro, y en caso afirmativo se reinicia la función.'''

def agregar_registro(diccionario):
  clave = input('\nIngrese nombre y apellido:')
  valor = int(input('Ingrese edad:'))
  diccionario[clave] = valor
  cargar_otro = input("Si desea cargar otro registro, ingrese 's' y presione Enter. De lo contrario, sólo presione Enter: ")
  if cargar_otro.lower() == 's':
    agregar_registro(diccionario)

# La función siguiente crea un array con Numpy que contiene las edades, cuenta aquellos que son mayores a 25 con la función count_nonzero, y retorna el valor obtenido.

def contar_mayores__de_25(diccionario):
    vector_edades = np.array(list(diccionario.values()))
    mayores_de_25 = np.count_nonzero(vector_edades > 25)
    return mayores_de_25

# A continuación se crea el diccionario y se ejecutan las funciones anteriores para obtener la información requerida:

dict_edad = {}
input('Presione Enter para comenzar a cargar registros al diccionario... ')
agregar_registro(dict_edad)
mayores_de_25 = contar_mayores__de_25(dict_edad)

# Por último, se analiza el resultado obtenido y se presenta junto al mensaje correspondiente:

if mayores_de_25 != 0:
    if mayores_de_25 == len(dict_edad):
      print(f'\nEn la lista provista, todas las personas ({len(dict_edad)}) son mayores de 25 años.')
    else:
      print(f'\nEn la lista provista, hay {mayores_de_25} persona/s mayor/es de 25 años.')
else:
    print(f'\nEn la lista provista, no hay ninguna persona mayor de 25 años.')

"""9) Escribir un programa que solicite al usuario ingresar una lista de precios de productos. Utilizando la biblioteca NumPy, el programa debe calcular y mostrar por pantalla la media y la desviación estándar de los precios ingresados."""

# Resolución Ej. 9:

print('-Cálculos con precios-\n')

import numpy as np

# Pide al usuario ingresar la lista de productos y precios según el formato indicado:
string_prod_prec = input("Ingrese la lista de productos y precios en pesos, utilizando el siguiente formato: 'producto1 precio1, producto2 precio2, ...' \n")

# Se crea una lista separando por ',' la cadena ingresada.
lista_prod_prec = list(string_prod_prec.strip().split(','))

lista_precios =[]

for prod_prec in lista_prod_prec:   # Se separa cada valor de la lista anteriormente generada, asilando el precio y agregándolo a una nueva lista que contiene sólo los precios (lista_precios).
  p, precio = prod_prec.split()
  lista_precios.append(float(precio))  # Al momento de agregar el elemento a la lista de precios, se convierte a float.

array_precios = np.array(lista_precios) # Se crea un vector con la lista de precios, para que la biblioteca NumPy pueda trabajar con él, para la presentación del resultado.

print(f'\nLa media de los precios es {round(np.mean(array_precios),2)}, y la desviación estándar de los mismos es {round(np.std(array_precios),2)}.')

"""10) Escribir un programa que cree un DataFrame llamado "ventas" que contenga la siguiente información de ventas de productos en una tienda durante una semana:

- Columnas: "Producto", "Cantidad", "Precio unitario"

- Filas:
Producto: "A", Cantidad: 10, Precio unitario: 5
Producto: "B", Cantidad: 5, Precio unitario: 9
Producto: "C", Cantidad: 12, Precio unitario: 3.50
Producto: "D", Cantidad: 8, Precio unitario: 7.50

a) Utilizando el DataFrame "ventas" filtrar y mostrar solo las filas donde la cantidad de productos vendidos es mayor o igual a 10.

b) Utilizando el DataFrame "ventas" filtrar y mostrar solo las filas donde el precio unitario es menor a 5.00.
"""

# Resolución Ej. 10:

print('-Datos de ventas-\n')

import pandas as pd

# Diccionario a partir del cual se genera el DataFrame.
dicc_ventas = {'Producto' : ['A','B','C','D'],
               'Cantidad' : [10, 5, 12, 8],
               'Precio unitario' : [5.0, 9.0, 3.50, 7.50]}

ventas = pd.DataFrame(dicc_ventas)  # Se crea el DataFrame utilizando los datos del diccionario anterior.

print('Productos que se vendieron 10 veces o más:\n')
print(ventas[ventas['Cantidad']>=10].to_string(index=False))  # Se imprime el primer resultado, aplicando el filtro solicitado.

print('\nProductos con precio menor a 5.00:\n')
print(ventas[ventas['Precio unitario']<5.0].to_string(index=False)) # Se imprime el segundo resultado, aplicando el filtro solicitado.

# Con el método to_string(index=False) se evita que aparezcan los números de índice a la izquierda al imprimir el DataFrame, para presentarlo más prolijamente.
