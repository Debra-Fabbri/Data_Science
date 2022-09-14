# Práctica Clase 2

"""1) Abrir el archivo "Emisiones_CO2.csv" y cargar sus datos en un diccionario."""

import os
archivo = open('Emisiones_CO2.csv', 'r')
# Imprimimos la primer linea para ver su contenido
for linea in archivo:
    print(linea)
    break

dicc_emisiones = {  'cod_pais' : [],
                    'nom_pais' : [],
                    'region' : [],
                    'anio' : [],
                    'co2' : [],
                    'co2_percapita' : []}

# con next son saltamos una fila
next(archivo)

#recorremos cada linea y por cada key agregamos los campos
for linea in archivo:
    linea = linea.strip()
    campos = linea.split('|')
    dicc_emisiones['cod_pais'].append(campos[0])
    dicc_emisiones['nom_pais'].append(campos[1])
    dicc_emisiones['region'].append(campos[2])
    dicc_emisiones['anio'].append(campos[3])
    dicc_emisiones['co2'].append(campos[4])
    dicc_emisiones['co2_percapita'].append(campos[5])


#nos aseguramos de que todos los datos se hayan cargado correctamente
dicc_emisiones

# luego, cerramos el archivo
archivo.close()




"""2) a) ¿Cuántas variables hay? <br>
b) ¿Qué tipos de datos usar para cada una? <br>
c) ¿Qué tipo de variables son? <br>
d) ¿Hay valores faltantes? <br>
e) ¿Cuál es el total de emisiones de CO2 para 'América Latina y Caribe' en el año 2010?"""

#2) a) ¿Cuántas variables hay? <br>
variables = len(dicc_emisiones.keys())
keysvar = list(dicc_emisiones.keys())

print("2. a) Hay", variables, "variables y son: ",keysvar)

#b) ¿Qué tipos de datos usar para cada una? <br>
#c) ¿Qué tipo de variables son? <br>

for i in dicc_emisiones.values():
    print(i[1000])

print('')

for i in dicc_emisiones.values():
    print(type(i[1000]))

#Vemos que a los numeros los toma como str, por eso haremos una transformacion



for i in range(len(dicc_emisiones['anio'])):
    dicc_emisiones['anio'][i] = int(dicc_emisiones['anio'][i])



for indice, elemento in enumerate(dicc_emisiones['co2']):
    elemento = elemento.replace('.', '')
    elemento = elemento.replace(',', '.')
    if elemento:
        elemento = float(elemento)
    else:
        elemento = None
    dicc_emisiones['co2'][indice] = elemento



for indice, elemento in enumerate(dicc_emisiones['co2_percapita']):
    elemento = elemento.replace('.', '')
    elemento = elemento.replace(',', '.')
    if elemento:
        elemento = float(elemento)
    else:
        elemento = None
    dicc_emisiones['co2_percapita'][indice] = elemento

#Volvemos a ver que tipo de datos tenemos
for i in dicc_emisiones.values():
    print(i[1000])

print('')

for i in dicc_emisiones.values():
    print(type(i[1000]))

#Finalmente vemos que ahora tenemos str, int, float


#d) ¿Hay valores faltantes? 

valores_falt = False

for i in dicc_emisiones.values():
    if None in i:
        valores_falt = True
        break
    else: 
        pass
    
if valores_falt == True: 
    print('Hay valores faltantes') 
else: 
    print('No hay valores faltantes')


#e) ¿Cuál es el total de emisiones de CO2 para 'América Latina y Caribe' en el año 2010?

filtro_region = 'América Latina y Caribe'
filtro_anio = 2010
total_emisiones = 0 

for indice, elemento in enumerate(dicc_emisiones['region']):
    if dicc_emisiones['region'][indice] == filtro_region and dicc_emisiones['anio'][indice] == filtro_anio and dicc_emisiones['co2'][indice] != None:
        total_emisiones += dicc_emisiones['co2'][indice]

print("El total de emisiones es de:", total_emisiones)