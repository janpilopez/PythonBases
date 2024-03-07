# Expresiones regulares
# Python tiene una librería muy
# poderosa llamada expresiones regulares que maneja varias de estas tareas de man-
# era bastante elegante. La razón por la que no presentamos las expresiones regulares
# antes se debe a que, aunque son muy poderosas, son un poco más complicadas y
# toma algo de tiempo acostumbrarse a su sintaxis.

# Búsqueda de líneas que contengan 'From'
import re
#Linux
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 
# man = open('C:/Users/jp/Documents/Python/archivos/mbox-short.txt')

for linea in man:
    linea = linea.rstrip()
    if re.search('From:', linea):
        print(linea)
        
# Abrimos el archivo, revisamos cada línea, y usamos la expresión regular search()
# para imprimir solo las líneas que contengan la cadena “From”. Este programa no
# toma ventaja del auténtico poder de las expresiones regulares, ya que podríamos
# simplemente haber usado line.find() para lograr el mismo resultado.

# El poder de las expresiones regulares se manifiesta cuando agregamos caracteres
# especiales a la cadena de búsqueda que nos permite controlar de manera más precisa
# qué líneas calzan con la cadena. Agregar estos caracteres especiales a nuestra
# expresión regular nos permitirá buscar coincidencias y extraer datos usando unas
# pocas líneas de código.
# Por ejemplo, el signo de intercalación (N. del T.: “caret” en inglés, corresponde
# al signo ˆ) se utiliza en expresiones regulares para encontrar “el comienzo” de una
# lína. Podríamos cambiar nuestro programa para que solo retorne líneas en que
# tengan “From:” al comienzo, de la siguiente manera:
# Búsqueda de líneas que contengan 'From'
print(' ----------------------- ')
import re
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 
for linea in man:
    linea = linea.rstrip()
    if re.search('^From:', linea):
        print(linea)
        
# Ahora solo retornará líneas que comiencen con la cadena “From:”. Este sigue siendo
# un ejemplo muy sencillo que podríamos haber implementado usando el método
# startswith() de la librería de cadenas. Pero sirve para presentar la idea de que
# las expresiones regulares contienen caracteres especiales que nos dan mayor control
# sobre qué coincidencias retornará la expresión regular.