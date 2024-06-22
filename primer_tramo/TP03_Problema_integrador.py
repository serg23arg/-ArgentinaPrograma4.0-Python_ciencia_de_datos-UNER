# -*- coding: utf-8 -*-
# Guía Práctica N° 3: Pipeline, Consultas e Informes




---

Los siguientes ejercicios implican el uso de los conceptos teóricos incluidos en los módulos II a IV del curso.
Para la realización de la guía se sugiere tener a mano el material desarrollado en clase.
Es importante que los ejercicios se resuelvan y entreguen de manera organizada.

## Objetivos
----

*   Aplicar un flujo de trabajo para responder las preguntas de investigación del proyecto de ciencia de datos.
*   Seleccionar datos desde una base de datos utilizando un lenguaje estructurado de consultas (*Structrued Query Language*) y DataFrames de pandas.
*   Aplicar las herramientas aprendidas en las guías anteriores para realizar algunas estimaciones sobre datos reales.
*   Expresar los hallazgos y respuestas a las preguntas de investigación en un informe gerencial que sirva de apoyo a la toma de decisiones.

# Problema de práctica

El siguiente enunciado te permitirá practicar los temas vistos. Y, para poner esto en el contexto del tema tratado (el alquiler de bicicletas compartidas), verás que está redactado como parte de un trabajo que es solicitado por un equipo de gestión al cual deberás brindarle finalmente respuestas y recomendaciones claras y concisas a partir de los datos.

Por una cuestión de practicidad, utilizaremos la misma base de datos que has empleado durante los ejercicios de clase la cual provee información del año 2011.

¡Aquí vamos!

## BikeShare

> La empresa "BikeShare" tiene un sistema de bicicletas compartidas en varias ciudades del mundo. Para mejorar el servicio y aumentar la satisfacción del usuario, se requiere un análisis de los datos de uso de las bicicletas. El objetivo de este análisis es entender mejor el comportamiento de los usuarios y las tendencias en el uso de las bicicletas compartidas.
>
> Para ello, se solicita al equipo de ciencia de datos de la empresa que realice una exploración y análisis de los datos de sus sistemas de bicicletas compartidas. La base de datos contiene información sobre los viajes, como la duración, la ubicación de inicio y fin, la hora del día y la fecha, entre otros datos.
>
> * Enlace a la base de datos: [bikeshare.db](https://drive.google.com/file/d/1hNBT1W0U5CtBuwV5WhSeQigy9vUhG9dp/view?usp=sharing)
>
> Se espera que el equipo utilice SQL, Python y pandas para realizar consultas y filtrar los datos para responder preguntas de investigación específicas siguientes:
>
> 1. ¿Cuál es la cantidad de viajes de los usuarios de tipo Miembro y de tipo Casual que duran 5 minutos o más?
2. ¿En qué bicicleta se realizó el viaje en bicicleta más largo? ¿Cuántos minutos duró ese viaje?
3. ¿Cuáles son los IDs de las 3 estaciones con la mayor duración de viajes que comienzan y terminan en la misma estación?
4. ¿Cuáles son los IDs de las 5 estaciones de partida que poseen los viajes de mayor duración de usuarios de tipo Miembro?
5. ¿Cuál es el nombre de la estación donde comienzan y terminan la mayoría de los paseos?
6. Grafica en un mapa las dos estaciones más populares (las que tienen mayor número de viajes que parten de ellas).
7. Muestra los primeros registros (head) de una tabla (DataFrame) con todos los viajes disponibles en la Base de Datos para usuarios Miembro. Posteriormente, grafica un histograma que permita comparar la cantidad de viajes agrupados por día de la semana.
>
> Una vez que el equipo haya realizado el análisis de los datos y haya encontrado patrones y tendencias relevantes, se espera que se **presente un informe gerencial** bien estructurado con los resultados y conclusiones a los que se arribaron. El informe debe incluir visualizaciones de los datos, gráficos y tablas para ayudar a explicar las conclusiones. La gerencia de BikeShare utilizará estos resultados para mejorar el servicio y hacerlo más eficiente.

## Entregables

Del enunciado anterior deberás generar dos entregables:

1. **El código con el que realiza el análisis de datos.** Puede ser esta mísma guía Colab con las modificaciones necesarias, o un nuevo Colab.
2. **El informe gerencial**, el cual deberá estar estructurado como se indicó en el apartado correspondiente.

Ambos entregables deben dar cuenta de la correcta aplicación del flujo de trabajo.

¡Cualquier inquietud, no dudes en consultar!

## **Solución**

---
"""

# Importación de bibliotecas y obtención de datos:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine, text, inspect

from google.colab import drive
drive.mount('/content/drive')

url = "sqlite:////content/drive/MyDrive/Curso Python Colab/bikeshare.db" #Editar según ruta actual
bikeshare = create_engine(url)

# Exploración de esquemas y tablas presentes en base de datos.

inspector = inspect(bikeshare)
schemas = inspector.get_schema_names()

for schema in schemas:
    print(f"Esquema:\n{schema}")
    print(f"\nTablas:")
    for nombre_tabla in inspector.get_table_names(schema=schema):
        print(nombre_tabla)

# Inspección de campos y tipos de datos respectivos, de cada tabla:

tabla1 = 'trip_data'
tabla2 = 'bikeshare_stations'

def info_tabla(tabla):
    print(f'Información de tabla "{tabla}":\n')
    columnas = inspector.get_columns(tabla)
    for columna in columnas:
      print(columna['name'], columna['type'])

info_tabla(tabla1)
print()
info_tabla(tabla2)

# Visualización de las primeras 10 filas de cada tabla
def primeras_filas(tabla):
    print('Tabla:', tabla)
    with bikeshare.connect() as conexion:
        DF = pd.read_sql(text('SELECT * FROM ' + tabla + ' LIMIT 10'), conexion)
        display(DF.head(10))
        registros = pd.read_sql(text('SELECT COUNT(*) FROM ' + tabla), conexion)
        print(f'Registros totales: {registros.iloc[0,0]}')
        print('\n')

primeras_filas('trip_data')
primeras_filas('bikeshare_stations')

# En esta celda se define una función para automatizar el pasaje de información de la base a un Dataframe.

def pasar_a_DF(consulta):
    with bikeshare.connect() as conexion:
        df = pd.read_sql(text(consulta), conexion)
    return df

# Solución pregunta 1) ¿Cuál es la cantidad de viajes de los usuarios de tipo Miembro y de tipo Casual que duran 5 minutos o más?

# Nótese que en la consulta SQL siguiente se agregó un filtro para que no incluya los registros en donde figura "Unknown" en el campo member_type,
# ya que anteriormente, al ejecutar la consulta sin esa condición, se encontraron dichos datos atípicos en la base.

consulta_1 = 'SELECT member_type AS Tipo_de_miembro, COUNT(*) AS viajes_5_min_o_mas FROM trip_data WHERE duration >= 300 AND Tipo_de_miembro != "Unknown" GROUP BY member_type ORDER BY viajes_5_min_o_mas DESC'

solucion_1 = pasar_a_DF(consulta_1)

display(solucion_1)

# Gráfica de la preguna 1)

print('Distribución de Viajes de 5 minutos o más, según Tipo de Miembro')
plt.figure(figsize=(4, 4))
plt.pie(solucion_1.viajes_5_min_o_mas, labels=solucion_1.Tipo_de_miembro, autopct='%1.1f%%', startangle=240)
# plt.savefig('figura_pregunta_1.jpg')
plt.show()

# Solución pregunta 2) ¿En qué bicicleta se realizó el viaje más largo? ¿Cuántos minutos duró ese viaje?

consulta_2 = 'SELECT bike_number, MAX(duration)/60 AS duracion_en_min FROM trip_data'

solucion_2 = pasar_a_DF(consulta_2)

solucion_2

# Esta celda es únicamente a fines de verificación de la respuesta de la celda anterior.

consulta_2_verificacion = 'SELECT *, duration/60 FROM trip_data ORDER BY duration DESC LIMIT 5'

solucion_2_verificacion = pasar_a_DF(consulta_2_verificacion)

solucion_2_verificacion

# Solución pregunta 3) ¿Cuáles son los IDs de las 3 estaciones con la mayor duración de viajes que comienzan y terminan en la misma estación?

consulta_3a = 'SELECT start_station AS ID_Estacion, duration/60 AS Duracion FROM trip_data WHERE start_station = end_station ORDER BY Duracion DESC LIMIT 3'

solucion_3a = pasar_a_DF(consulta_3a)

solucion_3a

# Gráfica de la preguna 3)

print('ID de las 3 estaciones de viaje de mayor duración, comenzando y finalizando en la misma.')

# En la siguiente línea se convierten los valores de la columna ID_Estacion a string, para que el gráfico lo considere una categoría
# y no un valor numérico, a fin de que la gráfica sea más prolija y de menores dimensiones.

solucion_3a['ID_Estacion'] = solucion_3a['ID_Estacion'].astype(str)

plt.figure(figsize=(6, 4))
plt.bar(solucion_3a.ID_Estacion, solucion_3a.Duracion, width=0.2, color='orange')
plt.xlabel('ID_Estacion')
plt.xticks(solucion_3a.ID_Estacion)
plt.ylim(1400, 1450)
plt.ylabel('Duracion (minutos)')
plt.grid()
# plt.savefig('figura_pregunta_3a.jpg')
plt.show()

# Aquí se calculó adicionalmente la misma pregunta anterior, pero de forma agregada,
# sumando todos los viajes que comienzan y terminan en la misma estación. Se debió pasar la duración a horas,
# ya que si se deja en segundos, o incluso minutos, los valores son demasiado altos para interpretarlos y/o gráficarlos.

consulta_3b = 'SELECT start_station AS ID_Estacion, SUM(duration)/60/60 AS Duracion FROM trip_data WHERE start_station = end_station GROUP BY ID_Estacion ORDER BY Duracion DESC LIMIT 3'

solucion_3b = pasar_a_DF(consulta_3b)

solucion_3b

# Gráfica de la preguna 3b)

print('ID de las 3 estaciones con viajes de mayor duración, comenzando y finalizando en la misma, de forma agregada.')

solucion_3b['ID_Estacion'] = solucion_3b['ID_Estacion'].astype(str)
plt.figure(figsize=(6, 4))
plt.bar(solucion_3b.ID_Estacion, solucion_3b.Duracion, width=0.2, color='pink')
plt.xlabel('ID_Estacion')
plt.xticks(solucion_3b.ID_Estacion)
plt.ylim(2000, 5000)
plt.ylabel('Duracion agregada (horas)')
plt.grid()
# plt.savefig('figura_pregunta_3b.jpg')
plt.show()

# Verificación de la celda anterior. A modo de ejemplo, se observa que hay 3135 registros de viajes comenzados
# y terminados en la estacion 31217, validando así el cálculo de la celda anterior (pregunta 3b).

consulta_3b_verificacion = 'SELECT start_station, end_station, duration AS duracion_de_viaje_SEG FROM trip_data WHERE start_station = end_station AND start_station = 31217 ORDER BY duracion_de_viaje_SEG DESC'

solucion_3b_verificacion = pasar_a_DF(consulta_3b_verificacion)

solucion_3b_verificacion

# Solución pregunta 4) ¿Cuáles son los IDs de las 5 estaciones de partida que poseen los viajes de mayor duración de usuarios de tipo Miembro?

consulta_4 = 'SELECT member_type, start_station AS ID_Estacion, duration/60 AS Duracion_Min FROM trip_data WHERE member_type = "Member" ORDER BY Duracion_Min DESC LIMIT 5'

solucion_4 = pasar_a_DF(consulta_4)

solucion_4

# Gráfica de la preguna 4)

solucion_4['ID_Estacion'] = solucion_4['ID_Estacion'].astype(str)

plt.figure(figsize=(6, 4))
plt.bar(solucion_4.ID_Estacion, solucion_4.Duracion_Min, width=0.5, color='blue')
plt.xlabel('ID_Estacion')
plt.xticks(solucion_4.ID_Estacion)
plt.ylim(1400, 1450)
plt.ylabel('Duracion (minutos)')
plt.grid()
# plt.savefig('figura_pregunta_4.jpg')
plt.show()

# Solución pregunta 5) ¿Cuál es el nombre de la estación donde comienzan y terminan la mayoría de los paseos?

consulta_5_start = 'SELECT start_station AS ID_estacion, COUNT(*) AS partidas_desde_estacion, bikeshare_stations.name AS nombre_de_estacion FROM trip_data JOIN bikeshare_stations ON start_station = station_id GROUP BY start_station ORDER BY partidas_desde_estacion DESC LIMIT 1'
consulta_5_end = 'SELECT end_station AS ID_estacion, COUNT(*) AS llegadas_a_estacion, bikeshare_stations.name AS nombre_de_estacion FROM trip_data JOIN bikeshare_stations ON end_station = station_id GROUP BY end_station ORDER BY llegadas_a_estacion DESC LIMIT 1'

solucion_5_start = pasar_a_DF(consulta_5_start)

solucion_5_end = pasar_a_DF(consulta_5_end)


display(solucion_5_start)
print()
display(solucion_5_end)

# Otro método para buscar el nombre de las estaciones en la tabla bikeshare_stations, sin usar JOIN:

estacion_de_partida = solucion_5_start.iloc[0,0].astype(str)
estacion_de_llegada = solucion_5_end.iloc[0,0].astype(str)

consulta_5_final_start = 'SELECT station_id AS station_id_partidas, name AS nombre_de_estacion FROM bikeshare_stations WHERE station_id = ' + estacion_de_partida
consulta_5_final_end = 'SELECT station_id AS station_id_llegadas, name AS nombre_de_estacion FROM bikeshare_stations WHERE station_id = ' + estacion_de_llegada

solucion_5_final_start = pasar_a_DF(consulta_5_final_start)
solucion_5_final_end = pasar_a_DF(consulta_5_final_end)

print()
display(solucion_5_final_start)
print()
display(solucion_5_final_end)

# Solución pregunta 6) Grafica en un mapa las dos estaciones más populares (las que tienen mayor número de viajes que parten de ellas)

!pip install --quiet ipyleaflet
from ipyleaflet import Map, Marker, AwesomeIcon

consulta_mayores_partidas = 'SELECT start_station, bikeshare_stations.name AS nombre_de_estacion, COUNT(*) AS cantidad_de_partidas, bikeshare_stations.latitude, bikeshare_stations.longitude FROM trip_data JOIN bikeshare_stations ON start_station = station_id GROUP BY start_station ORDER BY cantidad_de_partidas DESC LIMIT 2'

df_mayores_partidas = pasar_a_DF(consulta_mayores_partidas)

display(df_mayores_partidas)

lista_coordenadas = list(zip(df_mayores_partidas.latitude, df_mayores_partidas.longitude))

# A continuación se aplica el método de cálculo de promedios de longitudes y latitudes para determinar el centro del mapa,
# ya que al ser 2 puntos a graficar, el método es adecuado.

centro = (df_mayores_partidas.latitude.mean(), df_mayores_partidas.longitude.mean())

dcmap = Map(center=centro, zoom=12)

contador = 0
for coordenadas in lista_coordenadas:
      referencia = df_mayores_partidas.iloc[contador, 1]
      icon = AwesomeIcon(name='play', marker_color='blue', icon_color='green')
      marker = Marker(location=coordenadas, icon=icon, title=referencia)
      dcmap.add_layer(marker)
      contador += 1

display(dcmap)

# Solución pregunta 7) Muestra los primeros registros (head) de una tabla (DataFrame) con todos los viajes disponibles en la Base de Datos
# para usuarios Miembro. Posteriormente, grafica un histograma que permita comparar la cantidad de viajes agrupados por día de la semana.


with bikeshare.connect() as conexion:    # Se crea DF con toda la información de la tabla principal, para usuarios Member.
    df_miembros = pd.read_sql(text('SELECT * FROM trip_data WHERE member_type = "Member"'), conexion, parse_dates=['start_date', 'end_date'])

df_miembros['nro_dia'] = df_miembros['start_date'].apply(lambda x: x.weekday()) # Se utiliza la biblioteca datetime para colocar un número en una nueva columna, que represente el día de la semana, aplicando el método weekday() a cada valor del campo start_date.

# La siguiente pieza de código utiliza condicionales anidados para, según el nro. de día agregado anteriormente, se cree una nueva columna que traduzca dichos números al nombre del día que le corresponde.

df_miembros['dia'] = df_miembros['nro_dia'].apply(lambda x: 'Lunes' if x == 0 else (
                                                              'Martes' if x == 1 else (
                                                                'Miércoles' if x == 2 else (
                                                                  'Jueves' if x == 3 else (
                                                                    'Viernes' if x == 4 else (
                                                                      'Sábado' if x == 5 else (
                                                                        'Domingo' if x == 6 else 'N/A')))))))
print('Tabla trip_data / Primeros registros:')
display(df_miembros.head())

# Para la gráfica, se crea un nuevo DF descartando las columnas que no se necesitan.

columnas_descartar = ['index', 'duration', 'start_date', 'end_date', 'start_station', 'end_station', 'bike_number', 'member_type', 'nro_dia']
df_miembros_grafico = df_miembros.drop(columns = columnas_descartar)

plt.figure(figsize=(7, 5))
df_miembros_grafico['dia'].value_counts().sort_values().plot(kind='bar')
plt.title('Distribución de viajes por día de la semana')
plt.xlabel('Día')
plt.xticks(rotation=35, ha='right')
plt.ylabel('Cantidad de viajes')

for index, value in enumerate(df_miembros_grafico['dia'].value_counts().sort_values()):
    plt.text(index, value, str(value), ha='center', va='bottom')

# plt.savefig('figura_pregunta_7.jpg')
plt.show()
plt.close()

# Adicionalmente, se calculó la cantidad de viajes que ocurrieron en cada mes, para lo cual se crea
# el DF apropiado y posteriormente se grafica.

with bikeshare.connect() as conexion:
    df_viajes_mes = pd.read_sql(text('SELECT start_date FROM trip_data'), conexion, parse_dates=['start_date'])

df_viajes_mes['mes'] = df_viajes_mes['start_date'].dt.month

plt.figure(figsize=(10, 5))
df_viajes_mes['mes'].value_counts().sort_index().plot(kind='bar', color='purple')
plt.title('Distribución de viajes por mes')
plt.xlabel('Mes')
plt.xticks(rotation=0)
plt.ylabel('Cantidad de viajes')

for index, value in enumerate(df_viajes_mes['mes'].value_counts().sort_index()):
    plt.text(index, value, str(value), ha='center', va='bottom')

# plt.savefig('figura_viajes_mes.jpg')
plt.show()
