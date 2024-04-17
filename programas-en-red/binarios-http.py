# Leyendo archivos binarios con urllib
# A veces se desea obtener un archivo que no es de texto (o binario) tal como una
# imagen o un archivo de video. Los datos en esos archivos generalmente no son
# útiles para ser impresos en pantalla, pero se puede hacer fácilmente una copia de
# una URL a un archivo local en el disco duro utilizando urllib.
# El método consiste en abrir la dirección URL y utilizar read para descargar todo el
# contenido del documento en una cadena (img) para después escribir esa información
# a un archivo local, tal como se muestra a continuación:

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
man_a = open('portada.jpg', 'wb')
man_a.write(img)
man_a.close()

# Este programa lee todos los datos que recibe de la red y los almacena en la variable
# img en la memoria principal de la computadora. Después, abre el archivo
# portada.jpg y escribe los datos en el disco. El argumento wb en la función open()
# abre un archivo binario en modo de escritura solamente. Este programa funcionará
# siempre y cuando el tamaño del archivo sea menor que el tamaño de la memoria de la computadora.

# Aún asi, si es un archivo grande de audio o video, este programa podría fallar o al
# menos ejecutarse sumamente lento cuando la memoria de la computadora se haya
# agotado. Para evitar que la memoria se termine, almacenamos los datos en bloques
# (o buffers) y luego escribimos cada bloque en el disco antes de obtener el siguiente
# bloque. De esta forma, el programa puede leer archivos de cualquier tamaño sin
# utilizar toda la memoria disponible en la computadora.

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
man_a = open('portada.jpg', 'wb')
tamano = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break #Si ya no hay caracteres sale del bucle
    tamano = tamano + len(info) #Suma la cantidad de caracteres
    man_a.write(info) #Escribimos los caracteres por bloques cada 100,000
print(tamano, 'caracteres copiados.')
man_a.close()

# En este ejemplo, leemos solamente 100,000 caracteres a la vez, y después los escribimos
# al archivo portada.jpg antes de obtener los siguientes 100,000 caracteres de datos desde la web.