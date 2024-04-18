# Análisis de JSON
# El JSON se construye anidando diccionarios y listas según se necesite. En este
# ejemplo, vamos a representar una lista de usuarios en la que cada usuario es un
# conjunto de parejas clave-valor (es decir, un diccionario). De modo que tendremos
# una lista de diccionarios.
# En el programa siguiente, usaremos la librería integrada ‘json’ para analizar el
# JSON y leer los datos. Compáralo cuidadosamente con los datos y código XML
# equivalentes que usamos antes. El JSON tiene menos detalles, de modo que pode-
# mos saber de antemano que vamos a obtener una lista y que la lista es de usuarios
# y además que cada usuario es un conjunto de parejas clave-valor. El JSON es más
# conciso (una ventaja), pero también es menos auto-descriptivo (una desventaja).
import json
datos = '''
    [
        { "id" : "001",
          "x" : "2",
          "nombre" : "Chuck"
        },
        
        { "id" : "009",
          "x" : "7",
          "nombre" : "Brent"
        }
    ]
    '''
info = json.loads(datos)
print('Total de usuarios:', len(info))
for elemento in info:
    print('Nombre', elemento['nombre'])
    print('Id', elemento['id'])
    print('Atributo', elemento['x'])
# Código: https://es.py4e.com/code3/json2.py

# Si comparas el código que extrae los datos del JSON analizado y el del XML, verás
# que lo que obtenemos de ‘json.loads()’ es una lista de Python que recorreremos con
# un bucle for, y cada elemento dentro de esa lista es un diccionario de Python. Una
# vez analizado el JSON, podemos usar el operador índice de Python para extraer
# los distintos fragmentos de datos de cada usuario. No tenemos que usar la librería
# JSON para rebuscar a través del JSON analizado, ya que los datos devueltos son
# sencillamente estructuras nativas de Python.

# La salida de este programa es exactamente la misma que la de la versión XML
# anterior.
# Total de usuarios: 2
# Nombre Chuck
# Id 001
# Atributo 2
# Nombre Brent
# Id 009
# Atributo 7