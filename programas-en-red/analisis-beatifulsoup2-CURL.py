# Esta lista es mucho más larga porque algunas de las etiquetas de anclaje son rutas
# relativas (e.g., tutorial/index.html) o referencias dentro de la página (p. ej., ‘#’)
# que no incluyen “http://” o “https://”, lo cual era un requerimiento en nuestra
# expresión regular.

# También puedes utilizar BeautifulSoup para extraer varias partes de cada etiqueta de este modo:
# Para ejecutar este programa descarga BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4
# O descarga el archivo
# http://www.py4e.com/code3/bs4.zip
# y descomprimelo en el mismo directorio que este archivo

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Introduzca - ') #http://www.dr-chuck.com/page1.htm
html = urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, "html.parser")
# Obtener todas las etiquetas de anclaje, en este caso enlace (a)
etiquetas = sopa('a')
for etiqueta in etiquetas:
# Look at the parts of a tag
    print('ETIQUETA:', etiqueta)
    print('URL:', etiqueta.get('href', None)) # En este caso, etiqueta.get('href', None) busca el atributo 'href' en el objeto etiqueta. Si el atributo 'href' está presente en etiqueta, se devuelve su valor. Si el atributo 'href' no está presente en etiqueta, se devuelve el valor None.
    print('Contenido:', etiqueta.contents[0]) # En este caso específico, el contenido de la etiqueta <a> es simplemente el texto "Second Page". Por lo tanto, etiqueta.contents[0] se referiría al primer elemento dentro de los contenidos de la etiqueta <a>, que en este caso es el texto "Second Page"
    print('Atributos:', etiqueta.attrs)

#### Sección extra para usuarios de Unix / Linux

# Si tienes una computadora Linux, Unix, o Macintosh, probablemente tienes co-
# mandos nativos de tu sistema operativo para obtener tanto archivos de texto

# plano como archivos binarios utilizando los procolos HTTP o de Transferencia
# de Archivos (File Transfer - FTP). Uno de esos comandos es curl:
# $ curl -O http://www.py4e.com/cover.jpg
# El comando curl es una abreviación de “copiar URL” y por esa razón los dos

# ejemplos vistos anteriormente para obtener archivos binarios con urllib son as-
# tutamente llamados curl1.py y curl2.py en www.py4e.com/code3 debido a que

# ellos implementan una funcionalidad similar a la del comando curl. Existe tam-
# bién un programa de ejemplo curl3.py que realiza la misma tarea de forma un

# poco más eficiente, en caso de que quieras usar de verdad este diseño en algún
# programa que estés escribiendo.
# Un segundo comando que funciona de forma similar es wget:
# $ wget http://www.py4e.com/cover.jpg
# Ambos comandos hacen que obtener páginas web y archivos remotos se vuelva una
# tarea fácil.
