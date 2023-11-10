# -*- coding: utf-8 -*-

# Guía Práctica N° 2: Introducción al Pipeline de Ciencia de Datos

---

Los siguientes ejercicios implican el uso de los conceptos teóricos incluidos en los módulos II a III del curso.
Para la realización de la guía se sugiere tener a mano el material desarrollado en clase.
Es importante que los ejercicios se resuelvan y entreguen de manera organizada.

## Objetivos
----

*   Aprender a usar de manera más fluida las herramientas que nos proveen las bibliotecas de *NumPy*, *Matplotlib* y *Pandas*.
*   Emplear un flujo de trabajo para encarar de forma organizada los problemas de ciencia de datos, mediante uso de las herramientas provistas por los módulos de Python presentados.

# Ejercicios ✍ 🤓

# Ejercicio 1: Creación, lectura y análisis de un archivo con gustos musicales
---
Utilizando la Biblioteca Pandas, realice los siguientes pasos correspondientes al flujo de trabajo desarrollado.

1. **Obtención de datos**: Genere y posteriormente lea un archivo llamado "generos_musicales.csv". El mismo debe contener 4 columnas: Nombre, Edad (entre 12 y 75), País y Género musical (Electrónica, Jazz, Rock, Pop, Cumbia) y 25 filas correspondientes a los valores para cada columna.

2. **Análisis exploratorio y visualización**: Realice un análisis exploratorio de los datos:
- a) Indique la cantidad de personas para cada género musical.
- b) ¿Cuántas personas mayores de 35 años escuchan Rock?
- c) Determine en qué país se escucha más el género "Pop".
- d) Determine y mostrar el porcentaje de géneros musicales para personas entre 25 y 55 años.

3. **Limpieza de datos**: Elimine las filas con valores faltantes y las transacciones con cantidad negativa o cero (si es necesario).
"""

# Solución #1 / Obtención de datos:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

"""Link al csv: [generos_musicales.csv](https://drive.google.com/file/d/1oR4lhCuffSSdIApYUX2oYZSssMTDHarW/view?usp=sharing)"""

ruta = '/content/drive/MyDrive/Archivos auxiliares Curso Python/' # Editar

generos_musicales = pd.read_csv(ruta + "generos_musicales.csv", sep=';', encoding='latin-1')

# Análisis de información básica del dataset:
print(generos_musicales.info())
print('\n')
print(generos_musicales.head(5))

print('\nDe acuerdo a la información a la vista, no hay valores nulos en el dataset.')

# Solución #2 / Items a) - d):

# a)
print('\033[1ma) Indique la cantidad de personas para cada género musical:\033[0m\n')

print(generos_musicales['Género musical'].value_counts())

plt.figure(figsize=(5, 3))
generos_musicales["Género musical"].value_counts().sort_values().plot(kind="bar")
plt.title("Distribución de encuestados por Género musical")
plt.ylabel("Frecuencia")
plt.show()

# b)
generos_musicales_mayor_35 = generos_musicales[generos_musicales['Edad'] > 35]   #Se crean un nuevo DF, dejando de lado los registros que no interesan para esta consulta.
print(f"\n\033[1mb) Cantidad de personas mayores de 35 años que escuchan Rock:\033[0m {generos_musicales['Género musical'].value_counts()['Rock']}\n")

plt.figure(figsize=(5, 3))
generos_musicales_mayor_35["Género musical"].value_counts().sort_values().plot(kind="bar")
plt.title("Distribución de géneros musicales en mayores de 35 años")
plt.ylabel("Frecuencia")
plt.show()

# c)
print('\n\033[1mc) Determine en qué país se escucha más el género Pop:\033[0m')

generos_musicales_pop = generos_musicales[generos_musicales['Género musical'] == 'Pop'] # Se crea DF cuyos registros cumplen con la condición buscada.
print(f"El país en el que se escucha más Pop es {generos_musicales_pop['País'].value_counts().idxmax()}, con un total de {generos_musicales_pop['País'].value_counts().max()} ocurrencias.\n")

plt.figure(figsize=(5, 3))
generos_musicales_pop["País"].value_counts().sort_values().plot(kind="pie", autopct="%1.1f%%", ylabel="")
plt.title("Porcentaje de encuestados que escuchan Pop, según país")
plt.show()

# d)
print('\n\033[1md) Determinar y mostrar el porcentaje de géneros musicales para personas entre 25 y 55 años:\033[0m')

generos_musicales_25a55 = generos_musicales[(generos_musicales['Edad'] >= 25) & (generos_musicales['Edad'] <= 55)]  # Se crea DF cuyos registros cumplen con la condición buscada.
generos_musicales_25a55_porc = generos_musicales_25a55.groupby('Género musical').size().reset_index(name='Ocurrencias')   # En base al DF recientemente creado, se genera uno nuevo agrupando los géneros e informado el tamaño del mismo (cantidad de cada valor) con .size(), en una nueva columna llamada "Ocurrencias".
generos_musicales_25a55_porc['% del total'] = round((generos_musicales_25a55_porc['Ocurrencias'] / len(generos_musicales_25a55)) * 100, 1) #Se agrega una tercera columna, en donde se informa el porcentaje que representa cada genero del total.

print(f"A continuación se presenta la cantidad de ocurrencias de Género musical y el porcentaje que representan, del total de encuestados\n de 25 a 55 años ({len(generos_musicales_25a55)}):\n")
print(generos_musicales_25a55_porc)

plt.figure(figsize=(5, 3))
generos_musicales_25a55['Género musical'].value_counts().sort_values().plot(kind="pie", autopct="%1.1f%%", ylabel="")
plt.title("Distribución porcentual de Género musical, de los encuestados de 25 a 55 años")
plt.show()

# Solución #3 / Limpieza de datos: Si bien en este dataset no es necesario, la limpieza se ejecutaría de la siguiente forma:

generos_musicales = generos_musicales.dropna()  # Eliminar registros con valores nulos (NaN).
generos_musicales = generos_musicales[generos_musicales['Edad'] > 0 ] # Eliminar registros con edades negativas.

"""## Ejercicio 2: Análisis de datos de encuestas
---

Se le provee de un archivo llamado ["survey.csv"](https://drive.google.com/file/d/1iyBgTw1eviK0nFLBTzf1xGfDgLLRMjV4/view?usp=sharing) que contiene datos de una encuesta de satisfacción de clientes gestionada por una tienda.
Cada fila representa a un participante, su género,  un rango de edad, la ocupación y si posee una membresía, así como también las respuestas a diferentes preguntas de la encuesta.

Génder (género): Female/Male.

Age (edad): 0 (menor a 20 años) - 1 (20 a 29 años) - 2 (30 a 39 años) - 3 (igual o mayor a 40 años).

Occupation (ocupación): Student, Employed, Self-employed, Unemployed.

Card (tarjeta de membresía): Yes/No.

Las preguntas de la encuesta fueron:

Q1 (Pregunta 1): ¿Cómo calificaría la gama de precios del local? (1 = Muy malo, 5 = Excelente)

Q2 (Pregunta 2): ¿Qué importancia tienen las rebajas y las promociones en su decisión de compra? (1 = Muy poca, 5 = Mucha importancia)

Q3 (Pregunta 3): ¿Cómo calificaría el ambiente del local? (1 = Muy malo, 5 = Excelente)

Su objetivo es aplicar el siguiente flujo de trabajo para extraer información del dataset:

 **1) Obtención de datos**

**2) Análisis exploratorio y visualización**

**3) Limpieza de datos (si es necesario)**

**4) Elaboración de conclusiones breves sobre el trabajo realizado.**
"""

# Solución #1 / Obtención de datos
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

ruta = '/content/drive/MyDrive/Archivos auxiliares Curso Python/' # Editar

df_surveys = pd.read_csv(ruta + 'survey.csv')

# Solución #2 / Análisis exploratorio y visualización

print(df_surveys.info())
print('\n')
print(df_surveys.head(5))

print('\nDe la información obtenida, se identifican 2 valores nulos en la columna Age')

# Solución #3 / Limpieza de datos

columnas = list(df_surveys.columns)
columnas_str = []

for c in columnas:                     # Se confecciona una lista de los encabezados de las columnas del tipo 'O' (object).
  if df_surveys[c].dtype == 'O':
    columnas_str.append(c)

for c in columnas_str:         # Se imprimen por pantalla los valores únicos de cada columna tipo object.
  print(f"{c}:{sorted(df_surveys[c].unique())}")   # Con el modificador "sorted", las listas se imprimen alfabéticamente, siendo el espacio el primer caracter, para fácil reconocimiento.

# Con esta porción de código, se analizan las columnas tipo string en búsqueda de valores extraños.
print('\nSe observa en el resultado que en la columna Occupation hay al menos un valor no válido, que es un espacio.')

df_surveys = df_surveys.dropna()  # Eliminar filas con valores faltantes (NaN).
df_surveys = df_surveys[df_surveys['Occupation'] != ' '] # Eliminar filas con valores incoherentes;
                                                         # en este caso, celdas completadas con ' ' en la columna indicada.

# Solución #4 / Generación de nueva información y gráficos

# Se crea una columna cuyo valor informa el resultado final de la encuesta, en porcentaje,
# teniendo en cuenta que el máximo puntaje que una encuesta puede obtener es 15 (5 puntos por pregunta).

df_surveys['Score (%)'] = round(((df_surveys['Q1'] + df_surveys['Q2'] + df_surveys['Q3']) / 15)*100,1)

df_surveys

# Se presentan los datos descriptivos del dataframe:
print(df_surveys.describe())

print('\nAlgunas conclusiones preliminares:\n')
print('a) La pregunta que recibió menor puntaje, y por ende la que requiere mayor atención de parte de la tienda, es la Q1, con un promedio de 2.8, en la escala de 1 a 5.')
print('b) El promedio de Score general es satisfactorio, con una media de 73, mínimo de 53 y máximo de 100')

# A continuación se crean sub-dataframes, para generar luego los primeros gráficos:

df_surveys_gend = df_surveys.groupby('Gender')['Score (%)'].mean()
df_surveys_age = df_surveys.groupby('Age')['Score (%)'].mean()
df_surveys_occu = df_surveys.groupby('Occupation')['Score (%)'].mean()
df_surveys_card = df_surveys.groupby('Card')['Score (%)'].mean()

plt.figure(figsize=(5, 3))
df_surveys['Gender'].value_counts().sort_values().plot(kind="pie", autopct="%1.1f%%", ylabel="")
plt.title("Porcentaje de participación según Género")
plt.show()

plt.figure(figsize=(3, 3))
plt.bar(df_surveys_gend.index, df_surveys_gend)
plt.xlabel('Gender')
plt.ylabel('Score promedio')
plt.title('Score promedio según Género')
plt.grid()
plt.show()

plt.figure(figsize=(3, 3))
plt.bar(df_surveys_age.index, df_surveys_age)
plt.xlabel('Age')
plt.ylabel('Score promedio')
plt.title('Score promedio según rangos de edad')
plt.grid()
plt.show()

plt.figure(figsize=(4, 3))
plt.bar(df_surveys_occu.index, df_surveys_occu)
plt.xlabel('Occupation')
plt.ylabel('Score promedio')
plt.title('Score promedio según ocupación')
plt.grid()
plt.show()

plt.figure(figsize=(3, 3))
plt.bar(df_surveys_card.index, df_surveys_card)
plt.xlabel('Card')
plt.ylabel('Score promedio')
plt.title('Score promedio según membresía')
plt.grid()
plt.show()

"""**De los gráficos anteriores se deduce:**

1. Las mujeres suelen participar más en esta encuesta que los hombres, y tienen una mejor opinión general.

2. Los participantes del rango de edad "2" son los que menos conformes están a nivel general.

3. Los "Empleados" promedian menor puntaje general en comparación a "Independientes" y "Estudiantes".

4. Los clientes que poseen membresía dan en promedio un puntaje general mayor a aquellos que no lo son.

**Conclusión #1:** Se sugiere analizar las encuestas completadas por los clientes en rango de edad "2", y diseñar una nueva encuesta enfocada a dicho segmento del mercado.
"""

# Se grafican las respuestas de las preguntas Q1, Q2 y Q3:

import seaborn as sns

preguntas = df_surveys.columns[4:7]
num_preguntas = len(preguntas)

sns.set(style="whitegrid")
colors = sns.color_palette("Set1")

fig, axs = plt.subplots(1, 3, figsize=(8, 3))

for i, pregunta in enumerate(preguntas):

    sns.countplot(x=pregunta, data=df_surveys, ax=axs[i], palette=colors)
    axs[i].set_title(f'Q{i+1}')
    axs[i].set_xlabel('Respuesta')
    axs[i].set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()

"""**Conclusión #2:** Al analizar la **frecuencia de respuesta de cada pregunta**, observamos que la ***pregunta 1***, referida a la gama de precios del local, es la que obtuvo el menor puntaje general, y por lo tanto sería beneficioso analizar posibles maneras de poder ofrecer precios más económicos a los clientes.

Lo anterior se confirma al analizar los resultados de la ***pregunta 2***, referida a cuán importante es para el encuestado las promociones y rebajas de precio, donde se observa que la mayoría de los participantes respondieron que es muy importante (puntajes 4 y 5), eligiendo el resto puntaje 3, que es un valor relativamente alto en una escala de 5.

Por último, en la ***pregunta 3*** se observa que la mayoría opinó que el ambiente de la tienda es favorable (puntajes 3 a 5), excepto 1 participante que eligió puntaje 2. En este caso, dado que la muestra es reducida, se recomienda revisar la encuesta de dicho participante (si es que la misma posee comentarios cualitativos) para entender el motivo de su respuesta.

# Ejercicio 3: Análisis de datos de precios
---

En el dataset ['galletitas.csv'](https://drive.google.com/file/d/1DmTM90XSeOgAU_wxNczHuabOCMKNaoYk/view?usp=drive_link) se encuentran datos ventas de Galletitas incluidas en el Programa de Precios Cuidados del año 2021.

Su objetivo es realizar un análisis de datos utilizando las bibliotecas *Pandas*, *Matplotlib* y *Numpy* disponibles para Python, siguiendo el siguiente flujo de trabajo:


1.   **Obtención de datos:** Leer el archivo "galletitas.csv" que contiene información sobre ventas de diferentes productos, incluido su precio, descripción y presentación.

2.   **Análisis exploratorio y visualización:**  Realice un análisis exploratorio de los datos que:

a) Muestre las ventas totales de las galletitas de Tipo "Saladas".

b) Muestre la distribución de los Precios mediante un histograma.

c) Agrupe y contabilice la cantidad de Ventas por Tipo de galletitas.

d) Obtenga los 5 productos de menor Precio y otra de los 5 productos de mayor Precio.

e) Evalue si las variables Precio y Cantidad (presentación en gramos) muestran alguna relación.

f) Agregue una variable que consista en ingresos = ventas*precio. Analícela agrupando esta variable por Año.


4. **Limpieza de datos:** Elimine las filas con valores faltantes y/o datos incongruentes.


5. **Reducción de dimensionalidad:** Cree un DataFrame pivotado donde cada columna muestre las ventas por Tipo de galletitas.

5. **Interpretación de las representaciones gráficas y elaboración de conclusiones breves.**
"""

# Solución #1 / Obtención de datos
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

ruta = '/content/drive/MyDrive/Archivos auxiliares Curso Python/'  # Editar

df_galletitas = pd.read_csv(ruta + 'galletitas.csv')

# Información básica del dataset:

print(df_galletitas.info())
print('\n')
print(df_galletitas.head(5))

print('\n De acuerdo a la información, no hay valores nulos en las columnas del dataset.')

columnas = list(df_galletitas.columns)
columnas_str = []

for c in columnas:                     # Se confecciona una lista con los encabezados de las columnas tipo 'O'  (object).
  if df_galletitas[c].dtype == 'O':
    columnas_str.append(c)

for c in columnas_str:         # Se imprime por pantalla los valores únicos de las columnas tipo object.
  print(f"{c}:{sorted(df_galletitas[c].unique())}") # Con el modificador "sorted", las listas se imprimen alfabéticamente, con los espacios al principio de cada una, para fácil reconocimiento.

# Con esta porción de código se analizan las columnas tipo string/object en búsqueda de valores extraños.

print('\nSe observa en el resultado que:\n')
print('a) En la columna Producto, hay valores ingresados con diferencias de formato para informar lo mismo (Galletita)')
print('b) En la columna Descripción, hay valores que son sólo un espacio (' '), y hay diferencias de formato entre valores equivalentes ("Clasica" y "Clasicas")')
print('c) En las columnas Marca y Unidad, hay valores ingresados con un espacio adelante.')

# Solución #4 / Se procede a la limpieza de datos   (Nota: Al ejecutar esta celda, arroja unas advertencias que en primer momento no aparecian, igualmente el codigo se ejecuta correctamente)

df_galletitas = df_galletitas[df_galletitas['Descripcion'] != ' '] # Eliminar filas con valores incoherentes. En este caso, celdas completadas con ' ' en la columna indicada.

df_galletitas['Fecha'] = pd.to_datetime(df_galletitas['Fecha'])  # Se convierte la columna de fecha a tipo datetime

for column in ['Producto', 'Tipo', 'Descripcion', 'Marca', 'Unidad', 'Rubro']:
    df_galletitas[column] = df_galletitas[column].str.strip()  # Se eliminan espacios al final y al comienzo de cada valor de las columnas que contienen texto.

# Se buscan los valores de la columna Producto, reemplazando los iguales a 'Galletitas' o 'galletitas', por 'Galletita':
producto = {'Galletitas' : 'Galletita', 'galletitas': 'Galletita'}
df_galletitas['Producto'] = df_galletitas['Producto'].replace(producto)

# Se buscan los valores de la columna Descripción, reemplazando los iguales a 'Clasicas', por 'Clasica':
df_galletitas['Descripcion'] = df_galletitas['Descripcion'].replace({'Clasicas': 'Clasica'})

# Solución #2 / Items a) - f)

# a)
print('\033[1ma) Muestre las ventas totales de las galletitas de Tipo "Saladas":\033[0m\n')

df_galletitas_saladas = df_galletitas[df_galletitas['Tipo'] == 'Saladas']
print(f"Las ventas totales de las Galletitas Saladas fue de {df_galletitas_saladas['Ventas'].sum()}.")

ventas_por_tipo = df_galletitas.groupby('Tipo')['Ventas'].sum().reset_index()
plt.figure(figsize=(5, 4))
plt.bar(ventas_por_tipo['Tipo'], ventas_por_tipo['Ventas'], color='green')
plt.xlabel('Tipo')
plt.ylabel('Ventas')
plt.title('Ventas por Tipo')
plt.grid()
plt.show()

print('Se observa además que la mayor cantidad de ventas, por gran diferencia, fue alcanzada por las Galletitas Dulces.\nPor lo tanto, se puede considerar que las Galletitas Dulces es el producto estrella de esta compañía.')

# b)
print('\n\033[1mb) Muestre la distribución de los Precios mediante un histograma:\033[0m\n')
plt.hist(df_galletitas['Precio'], bins=10, color= 'yellow')
plt.xlabel('Precio')
plt.xticks(list(range(20, 121,10)))
plt.ylabel('Frecuencia')
plt.title('Distribución general de Precios')
plt.grid()
plt.show()

print('El gráfico indica que la mayoría de los productos poseen precios medios (~$50 a ~$70), y en segundo lugar precios económicos ($20 a ~40$).')

# c)
print('\n\033[1mc) Agrupe y contabilice la cantidad de Ventas por Tipo de galletitas:\033[0m\n')

print(ventas_por_tipo.sort_values(by='Ventas', ascending=False).to_string(index=False))
print('(Gráfico en solución ítem a)')

# d)
print('\n\033[1md) Obtenga los 5 productos de menor Precio y los 5 productos de mayor Precio:\033[0m\n')

# A continuación, se crea una nueva columna combinando Marca y Descripción, ya que si se realiza el calculo de
# los 5 mayores o menores, como la tabla presenta datos de ventas, pueden haber valores duplicados.
# Luego de crear dicha columna, se eliminan las filas con duplicados en la misma, y se
# reduce la dimensionalidad de la tabla a solo dos columnas(Marca-Desc y Precio)

df_galletitas['Marca - Desc'] = df_galletitas['Marca']+" - "+df_galletitas['Descripcion']
df_galletitas_precio_x_prod = df_galletitas.drop_duplicates(subset='Marca - Desc')
df_galletitas_precio_x_prod = df_galletitas_precio_x_prod[['Marca - Desc','Precio']]
mayor_precio = df_galletitas_precio_x_prod.nlargest(5, 'Precio')   # Se crea DF con los 5 productos de mayor precio.
menor_precio = df_galletitas_precio_x_prod.nsmallest(5, 'Precio')  # Se crea DF con los 5 productos de menor precio.

print('Los 5 productos de menor precio son:\n')
print(menor_precio.sort_values(by='Precio', ascending = True).to_string(index=False))
print('\nLos 5 productos de mayor precio son:\n')
print(mayor_precio.sort_values(by='Precio', ascending = False).to_string(index=False))

# e)
print('\n\033[1me) Evalue si las variables Precio y Cantidad (presentación en gramos) muestran alguna relación:\033[0m\n')

coef_precio_cantidad = np.corrcoef(df_galletitas['Cantidad'], df_galletitas['Precio'])[0, 1]
print(f'El coeficiente de correlación entre Cantidad y Precio, de valor {round(coef_precio_cantidad,2)}, indica que la relación, si bien es positiva,\nes débil. Pueden existir productos elaborados que aunque la cantidad de su packaging es reducida,\nposeen un alto precio, como se puede apreciar en el siguiente gráfico:')

plt.figure(figsize=(9, 5))
plt.scatter(df_galletitas['Cantidad'],df_galletitas['Precio'])
plt.ylabel('Precio')
plt.xlabel('Cantidad')
plt.title('Relación entre Cantidad y Precio')
plt.grid()
plt.show()

# f)
print('\n\033[1mf) Agregue una variable que consista en ingresos = ventas*precio. Analícela agrupando esta variable por Año:\033[0m\n')

df_galletitas['Ingresos'] = df_galletitas['Ventas'] * df_galletitas['Precio']
df_galletitas['Año'] =  df_galletitas['Fecha'].dt.year   # Se crea columna año para un manejo más sencillo.
df_galletitas_ingresos_x_año = df_galletitas.groupby('Año')['Ingresos'].sum().reset_index()

plt.figure(figsize=(6, 3))
plt.plot(df_galletitas_ingresos_x_año['Año'], df_galletitas_ingresos_x_año['Ingresos'], color='black')
plt.xlabel('Año')
plt.xticks(df_galletitas_ingresos_x_año['Año'])
plt.ylabel('Ingresos')
plt.title('Ingresos de la venta de galletitas, desde 2020 a 2023')
plt.grid()
plt.show()

print('Se observa que del 2020 al 2021, la venta de galletitas se incremento notoriamente. Sin embargo, desde 2021 hasta 2022,\nlas ventas cayeron hasta casi el volumen de 2020, y se observa que desde entonces hay un indicio de recuperación.')

# Solución 6 / Interpretación de las representaciones gráficas y elaboración de conclusiones breves.

# Las interpretaciones y conclusiones ya se encuentran incluidas junto a los gráficos, en Solución #2.
