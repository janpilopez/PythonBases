# Análisis de HTML mediante BeautifulSoup
# A pesar de que HTML es parecido a XML1 y que algunas páginas son construidas
# cuidadosamente para ser XML, la mayoría del HTML generalmente está incom-
# pleto, de modo que puede causar que un analizador de XML rechace una página
# HTML completa por estar formada inadecuadamente.
# Hay varias librerías en Python que pueden ayudarte a analizar HTML y extraer
# datos de las páginas. Cada una tiene sus fortalezas y debilidades, por lo que puedes
# elegir una basada en tus necesidades.
# Por ejemplo, vamos a analizar una entrada HTML cualquiera y a extraer enlaces
# utilizando la librería BeautifulSoup. BeautifulSoup tolera código HTML bastante
# defectuoso y aún así te deja extraer los datos que necesitas. Puedes descargar e
# instalar el código de BeautifulSoup desde:
# https://pypi.python.org/pypi/beautifulsoup4

# Para ejecutar este programa descarga BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4
# O descarga el archivo
# http://www.py4e.com/code3/bs4.zip
# y descomprimelo en el mismo directorio que este archivo
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Introduzca - ')  #https://docs.python.org
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')
# Recuperar todas las etiquetas de anclaje
etiquetas = sopa('a')
for etiqueta in etiquetas:
    print(etiqueta.get('href', None))
