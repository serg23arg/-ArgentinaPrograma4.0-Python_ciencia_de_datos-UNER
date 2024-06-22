# -*- coding: utf-8 -*-
# Guía Práctica N° 1: Estructuras de Datos y POO




---

## Objetivos
----

- Comprender y aplicar las distintas estructuras de datos para resolver problemas relacionados  con las ciencias de datos.
- Aprender a representar y manipular datos de manera eficiente utilizando estructuras como arreglos, listas, diccionarios y grafos.
- Desarrollar habilidades de programación orientada a objetos para la creación y gestión de tipos de datos abstractos.

# Ejercicios ✍ 🤓

1) Escribir un programa que a partir de una lista de números cuente cuántas veces aparece un número específico en la lista.
"""

# Resolución

lista_numeros = [1,1,1,2,3,3,3,3,4,4,5,5,5,5,5,5]  # Lista a trabajar
dicc_num = {}

# En el siguiente bucle, si el número no está en el diccionario, se agrega y se le asigna el valor 1. En caso de que exista, se le suma 1 a su valor.
for n in lista_numeros:
 if n in dicc_num.keys():
  dicc_num[n] += 1
 else:
  dicc_num[n] = 1

print('Frecuencia de aparición de los elementos de la lista:\n\nElemento : Q')  # Se presenta el resultado

for num, fq in dicc_num.items():
   if fq == 1:
    print(f'{num}: {fq} vez')
   else:
    print(f'{num}: {fq} veces')

"""2) Escribir un programa que tome una lista y elimine los elementos duplicados, dejando solo los elementos únicos."""

# Resolución

lista_2 = ['a',7,'hola','x','a','x','x',7,9]  # Lista de elementos con duplicados.

# La siguiente función crea una lista alternativa, y con el bucle FOR recorre la lista a trabajar, agregando el elemento a la lista_unicos sólo si ya no existe dicho elemento.

def limpiar_lista(lista):
  lista_unicos = []

  for e in lista:
    if e not in lista_unicos:
      lista_unicos.append(e)

  return lista_unicos

lista_2_unicos = limpiar_lista(lista_2)   # Se crea lista nueva solo con los valores únicos y se presenta el resultado.

print(f'Lista original: {lista_2}')
print(f'Lista sin duplicados: {lista_2_unicos}')

"""3) Escribir un programa que tome una cadena de texto y cuente cuántas veces aparece cada palabra. El programa debe almacenar los resultados en un diccionario."""

# Resolución

cadena = input('Ingrese texto para analizar: ')

palabra = ""
lista_palabras =[]
filtro = (' ','.',',',';','-','¿','?','¡','!','/','(',')','_',':',"'",'"')
caracteres = 0
contador = 0
dicc_lower = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','Ñ':'ñ','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z','Á':'á','É':'é','Í':'i','Ó':'ó','Ú':'ú'}

for c in cadena:     # Se recorre la cadena ingresada por el usuario y se almacena el total de caracteres en una variable.
    caracteres += 1

for c in cadena:                                 # Se vuelve a recorrer la cadena, y como primer paso se pasa a minúscula si es necesario.
    contador += 1                                # Luego, si el caracter no está incluido en la tupla 'filtro', se reconoce como válido y
    if c in dicc_lower.keys():                   # se suma a la variable 'palabra'. Este proceso se repite siempre y cuando no se encuentre
      c = dicc_lower[c]                          # un caracter no válido, en cuyo caso se considera que la palabra finalizó, agregando entonces la misma
    if c not in filtro:                          # a la lista_palabras. Por otra parte, también se analiza que, al momento de agregar una palabra a la lista,
        palabra = palabra + c                           # dicha variable no se encuentre vacía. Este detalle evita que al encontrar dos caracteres no válidos
        if contador == caracteres and palabra != "":    # seguidos, se agregue un "vacío" a la lista de palabras. Por último, la función también
            lista_palabras.append(palabra)              # considera el momento en el que alcanza el fin de la cadena, en cuyo caso, si hay alguna palabra
    elif palabra != "":                                 # almacenada en dicha variable, no se omita y se agregue a la lista correctamente.
        lista_palabras.append(palabra)
        palabra = ""

print(lista_palabras)

dicc_palabras = {}                  # Se crea diccionario con cada palabra como clave, y como valor la cantidad que vaya
                                    # encontrando de cada una en la lista de palabras.
for palabra in lista_palabras:
 if palabra in dicc_palabras.keys():
  dicc_palabras[palabra] += 1
 else:
  dicc_palabras[palabra] = 1

print(f'\nPalabra : Repeticiones\n------- : ------------')
for clave, valor in dicc_palabras.items():
    print(f'{clave}: {valor}')

"""4) Escribir un programa que genere un arreglo con 30 números aleatorios. El programa debe calcular el promedio y la desviación estándar de los elementos en el arreglo."""

# Resolución
import numpy as np

num_al = np.random.rand(30)
cant_num = 0
sumatoria = 0

for n in num_al:
  cant_num += 1
  sumatoria += n

promedio = sumatoria / cant_num
sumatoria_terminos = 0

for n in num_al:
    sumatoria_terminos += (n - promedio)**2

desviacion = (sumatoria_terminos/cant_num)**0.5

print(f'Promedio: {promedio}')
print(f'Desviación Std: {desviacion}')
print('\nComprobación usando método .mean() y .std() de Numpy:')
print('Promedio:', np.mean(num_al))
print('Desviación Std:', np.std(num_al))

"""5) Escribir un programa que a partir de un arreglo de números, encuentre los índices de los 2 valores mínimos del arreglo."""

# Resolución
import numpy as np

arreglo_min = np.array([271, 7, 2, 9, 15, 34, 8, 12, 23, 54])

max = arreglo_min[0]

for num in arreglo_min:     # Aquí se determina el máximo número del arreglo.
  if num > max:
    max = num

max_ajustado = max + 1    # Se crea un máximo ajustado, sumándole 1. Esto se hace así ya que, de acuerdo a experimentación,
                          # noté que lo más seguro, si se está buscando un mínimo, sea tomar como valor de referencia para comenzar el máximo,
min1 = max_ajustado       # y el +1 asegura que se encuentren resultados en un caso supuesto en donde todos los valores son iguales.
min2 = max_ajustado       # Por otra parte, en los primeros intentos utilizando como valor de referencia el primero de la lista, posicion[0],
                          # con el método que estoy utilizando para calcular los dos índices, si el segundo menor se encontraba en posicion[1],
posicion_min1 = 0         # el programa no lo encontraba, y volvia a repetir el primer resultado.
posicion_min2 = 0
validacion = []           # A esta lista se va agregando elemento mínimo detectado en los siguientes bucles, para qué sucesivamente puedan
                          # ser omitidos de la búsqueda si se necesita buscar varios mínimos.
indice = 0                    # De acuerdo a la consigna, no se utilizaron métodos de Python para búsqueda de indices.

for num in arreglo_min:
  if num < min1:
     min1 = num
     posicion_min1 = indice
  indice += 1
validacion.append(posicion_min1)

indice = 0

for num in arreglo_min:
  if indice not in validacion:
    if num < min2:
       min2 = num
       posicion_min2 = indice
  indice += 1

print(f'El mínimo número del arreglo es {min1}, cuyo índice en el arreglo es {posicion_min1}')
print(f'El segundo menor es {min2}, cuyo índice en el arreglo es {posicion_min2}')

"""6) Clase Pila:
Crear una clase *Pila* con atributos de tamaño y elementos. Implementar métodos para añadir, remover y consultar elementos en el tope de la pila. Escribir un programa que utilice la pila para invertir el orden de una serie de números ingresados por el usuario.
"""

# Resolución

class Pila:
  def __init__(self):
    self.tamanio = 10
    self.lista_pila = []
    self.posicion = -1              # Atributo que sirve para identificar en qué posición de la lista se encuentra el tope de pila.

  def contar(self):
    cant_elementos = 0
    for e in self.lista_pila:
      cant_elementos += 1
    return cant_elementos

  def agregar(self, elemento = None):                                  # Se crea una función con doble uso. Primero si no se ingresa ningún elemento como parámetro,
    if elemento == None:                                               # la función pide al usuario que ingrese el valor a agregar a la pila de forma manual.
      if self.tamanio > self.posicion + 1:                             # En caso que se indique un parámtro, la función lo agrega directamente a la pila.
        self.lista_pila.append(input('Ingrese elemento para agregar a la pila:'))
        self.posicion += 1
        print('Elemento agregado.\n')                                  # En ambos casos, cuando la pila se llena, se arroja mensaje de error. De lo contrario,
        otro = input('¿Desea agregar otro elemento? (s/n)')            # se ofrece la posibilidad de agregar otro valor. Al agregar un valor, se actualiza la variable 'posicion'.
        if otro.lower() == 's':
          return self.agregar()
      else:
        print('La pila está llena.')
    else:
       if self.tamanio > self.posicion + 1:
        self.lista_pila.append(elemento)
        self.posicion += 1
       else:
        print('La pila está llena.')

  def eliminar(self, silent = False):                                       # En este caso, si se agrega el parametro silent configurado en True, como en el ejericio siguiente,
    if silent == False:                                                     # en lugar mostrar una interfaz al usuario con sus respectivos mensajes, directamente elimina el elemento.
      if self.posicion >= 0:                                                # Esta característica es práctica para poder manipular la pila desde un programa automatizado y evitar la necesidad de interacción.
        print(f'Elemento {self.lista_pila[self.posicion]} eliminado.\n')
        self.lista_pila.pop(self.posicion)
        self.posicion -= 1
        otro = input('¿Desea eliminar otro elemento? (s/n)')
        if otro.lower() == 's':
          return self.eliminar()
      else:
        print('La pila está vacía.')
    else:
      self.lista_pila.pop(self.posicion)
      self.posicion -= 1

  def consultar(self, silent = False):             # Similar a la función anterior, si desde un programa se llama a esta función con el parametro silent = True,
    if silent == False:                            # sólo se retorna el tope de pila, sin ningún mensaje dirigido al usuario.
      if self.posicion >= 0:
        print(f"El elemento en el tope de la pila es '{self.lista_pila[self.posicion]}'.")
      else:
        print('La pila está vacía.')
    else:
      return self.lista_pila[self.posicion]

pila1 = Pila()

pila1.agregar(5)

pila1.consultar()

pila1.eliminar()

print(pila1.lista_pila)
pila1.consultar()

# Programa para invertir orden de una lista usando la clase Pila

str_usuario = input("Ingrese una lista de números a trabajar separados por comas ',' y/o espacios ' ' (Máximo 10 números):")

elemento = ""
lista_usuario = []                          # Esta sección funciona de forma similar al ejercicio 3, para detectar los números ingresados
separadores = ', '                          # por el usuario y agregarlos a una lista, convirtiéndolos en el proceso a valores numéricos (int).
caracteres = 0
contador = 0
pila2 = Pila()
lista_usuario_invertida = []

for c in str_usuario:
    caracteres += 1

for c in str_usuario:
    contador += 1
    if c not in separadores:
        elemento = elemento + c
        if contador == caracteres and elemento != "":
            lista_usuario.append(int(elemento))
    elif elemento != "":
        lista_usuario.append(int(elemento))
        elemento = ""

for e in lista_usuario:     # Se transfieren los elementos de la lista ingresada a la pila.
  pila2.agregar(e)

elementos_en_pila = pila2.contar()    # Se obtiene la cantidad de elementos en la pila.

while elementos_en_pila > 0:
  lista_usuario_invertida.append(pila2.consultar(silent = True))         # Se agrega el elemento en tope de pila a la lista invertida
  pila2.eliminar(silent = True)                                          # y se lo elimina de la pila. Se usa la opción silent de las funciones.
  elementos_en_pila -= 1

print('Lista original:',lista_usuario)
print('Lista invertida:',lista_usuario_invertida)

"""7) Clase Cuenta Bancaria:
Crear una clase *CuentaBancaria* con atributos de saldo y número de cuenta. Implementar métodos para depositar, retirar dinero, y mostrar el saldo final.

"""

# Resolución

class CuentaBancaria:

  def __init__(self, nro_cuenta:str):
    self.nro_cuenta = nro_cuenta
    self.saldo = 0

  def depositar(self):
    importe = int(input('Ingrese importe a depositar:'))
    self.saldo += importe
    print(f'Operación de depósito completada.')
    print(f'Nuevo saldo: ${self.saldo}')

  def retirar(self):
    importe = int(input('Ingrese importe a retirar:'))
    if importe <= self.saldo:                              # Se valida, antes de realizar la operación de retiro, que la cuenta posea suficientes fondos.
      self.saldo -= importe                                # En caso contrario, se arroja mensaje de error y se ofrece reintentar.
      print('Operación de retiro completada.')
      print(f'Nuevo saldo: ${self.saldo}')
    else:
      print('Su cuenta no posee los fondos necesarios para realizar la operación.')
      self.consultar()
      reintento = input('¿Reintentar?  (s/n)')
      if reintento.lower() == 's':
        self.retirar()

  def consultar(self):
    print(f'El saldo de su cuenta {self.nro_cuenta} es de ${self.saldo}.')

cuenta1 = CuentaBancaria('1111-5262352/015')

cuenta1.consultar()

cuenta1.depositar()

cuenta1.retirar()

cuenta1.consultar()
