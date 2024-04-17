#Aunque podemos enviar y recibir datos manualmente mediante HTTP utilizando
# la librería socket, existe una forma mucho más simple para realizar esta habitual
# tarea en Python, utilizando la librería urllib.

# Utilizando urllib, es posible tratar una página web de forma parecida a un archivo.
# Se puede indicar simplemente qué página web se desea recuperar y urllib se en-
# cargará de manejar todos los detalles referentes al protocolo HTTP y a la cabecera.
# El código equivalente para leer el archivo romeo.txt desde la web usando urllib
# es el siguiente:
import urllib.request #Alternativa al codigo del protocolo-http
man_a = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for linea in man_a:
    print(linea.decode().strip())
    
# Una vez que la página web ha sido abierta con urllib.urlopen, se puede tratar
# como un archivo y leer a través de ella utilizando un bucle for.
# Cuando el programa se ejecuta, en su salida sólo vemos el contenido del archivo.
# Las cabeceras siguen enviándose, pero el código de urllib se encarga de manejarlas
# y solamente nos devuelve los datos.

# Como ejemplo, podemos escribir un programa para obtener los datos de romeo.txt
# y calcular la frecuencia de cada palabra en el archivo de la forma siguiente:
import urllib.request, urllib.parse, urllib.error
man_a = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
contadores = dict()
for linea in man_a:
    palabras = linea.decode().split()
    for palabra in palabras:
        contadores[palabra] = contadores.get(palabra, 0) + 1
print(contadores)

# Aunque en tu caso específico solo estés utilizando la funcionalidad de urllib.request, 
# es una buena práctica importar todas las librerías necesarias al comienzo de tu código. 
# Esto proporciona claridad y evita confusiones si en algún momento necesitas utilizar otras 
# funciones de las librerías adicionales. Además, en ocasiones futuras, podrías ampliar tu
# código para incluir funcionalidades que requieran las otras librerías importadas.