# Aplicación No 1: Servicio web de geocodifi-
# cación de Google

# Google tiene un excelente servicio web que nos permite hacer uso de su enorme
# base de datos de información geográfica. Podemos enviar una cadena de búsqueda
# geográfica, como “Ann Arbor, MI” a su API de geocodificación y conseguir que
# Google nos devuelva su mejor suposición sobre donde podría estar nuestra cadena
# de búsqueda en un mapa, además de los puntos de referencia en los alrededores.
# El servicio de geocodificación es gratuito, pero limitado, de modo que no se puede
# hacer un uso intensivo de esta API en una aplicación comercial. Pero si tienes cier-
# tos datos estadísticos en los cuales un usuario final ha introducido una localización
# en formato libre en un cuadro de texto, puedes utilizar esta API para limpiar esos
# datos de forma bastante efectiva.
# Cuando se usa una API libre, como la API de geocodificación de Google, se debe
# ser respetuoso con el uso de los recursos. Si hay demasiada gente que abusa del
# servicio, Google puede interrumpir o restringir significativamente su uso gratuito.
# Puedes leer la documentación online de este servicio, pero es bastante sencillo y
# puedes incluso probarlo desde un navegador, simplemente tecleando la siguiente
# URL en él:
# http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
# Asegúrate de limpiar la URL y eliminar cualquier espacio de ella antes de pegarla
# en tu navegador.
# La siguiente es una aplicación sencilla que pide al usuario una cadena de búsqueda,
# llama a la API de geocodificación de Google y extrae información del JSON que nos devuelve.

import urllib.request, urllib.parse, urllib.error
import json
import ssl
clave_api = False
# Si tienes una clave API de Google Places, ingresala aquí
# clave_api = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
if clave_api is False:
    clave_api = 42
    url_de_servicio = 'http://py4e-data.dr-chuck.net/json?'
else :
    url_de_servicio = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    direccion = input('Ingresa una ubicación: ')
    if len(direccion) < 1: break

    parms = dict()
    parms['address'] = direccion
    if clave_api is not False: parms['key'] = clave_api
    url = url_de_servicio + urllib.parse.urlencode(parms)
    
    print('Recuperando', url)
    uh = urllib.request.urlopen(url, context=ctx)
    datos = uh.read().decode()
    print('Recuperados', len(datos), 'caracteres')

    try:
        js = json.loads(datos)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Error al Recuperar ====')
        print(datos)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)

# Código: https://es.py4e.com/code3/geojson.py
# El programa toma la cadena de búsqueda y construye una URL codificándola
# como parámetro dentro de ella, utilizando luego ‘urllib’ para recuperar el texto de
# la API de geocodificación de Google. A diferencia de una página web estática, los
# datos que obtengamos dependerán de los parámetros que enviemos y de los datos
# geográficos almacenados en los servidores de Google.

# Una vez recuperados los datos JSON, los analizamos con la librería ‘json’ y re-
# visamos para asegurarnos de que hemos recibido datos válidos. Finalmente, ex-
# traemos la información que buscábamos.

# Puedes descargar www.py4e.com/code3/geoxml.py para revisar las variantes JSON
# y XML de la API de geocodificación de Google.