# Análisis the HTML y rascado de la web

# Uno de los usos más comunes de las capacidades de urllib en Python es rascar
# la web. El rascado de la web es cuando escribimos un programa que pretende ser
# un navegador web y recupera páginas, examinando luego los datos de esas páginas
# para encontrar ciertos patrones.
# Por ejemplo, un motor de búsqueda como Google buscará el código de una página
# web, extraerá los enlaces a otras paginas y las recuperará, extrayendo los enlaces
# que haya en ellas y así sucesivamente. Utilizando esta técnica, las arañas de Google
# alcanzan a casi todas las páginas de la web.

# Google utiliza también la frecuencia con que las páginas que encuentra enlazan ha-
# cia una página concreta para calcular la “importancia” de esa página, y la posición
# en la que debe aparecer dentro de sus resultados de búsqueda.

# Análisis de HTML mediante expresiones regulares

# Una forma sencilla de analizar HTML consiste en utilizar expresiones regulares
# para hacer búsquedas repetitivas que extraigan subcadenas coincidentes con un
# patrón en particular. Aquí tenemos una página web simple:
# <h1>La Primera Página</h1>
# <p>
# Si quieres, puedes visitar la
# <a href="http://www.dr-chuck.com/page2.htm">
# Segunda Página</a>.
# </p>

# Podemos construir una expresión regular bien formada para buscar y extraer los
# valores de los enlaces del texto anterior, de esta forma:
## href="http[s]?://.+?"

# Nuestra expresión regular busca cadenas que comiencen con “href="http://” o
# “href="https://”, seguido de uno o más caracteres (.+?), seguidos por otra comilla
# doble. El signo de interrogación después de [s]? indica que la coincidencia debe
# ser hecha en modo “no-codicioso”, en vez de en modo “codicioso”. Una búsqueda
# no-codiciosa intenta encontrar la cadena coincidente más pequeña posible, mientras
# que una búsqueda codiciosa intentaría localizar la cadena coincidente más grande.
# Añadimos paréntesis a nuestra expresión regular para indicar qué parte de la ca-
# dena localizada queremos extraer, y obtenemos el siguiente programa:

import urllib.request, urllib.parse, urllib.error
import re
import ssl
# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduzca - ')  # https://docs.python.org
html = urllib.request.urlopen(url).read()
# leer los datos de la web y buscar solo los enlaces, los parenteces indican que solo extrae y selecciona los enlaces
enlaces = re.findall(b'href="(http[s]?://.*?)"', html) #b o .encode()
for enlace in enlaces:
    print(enlace.decode())