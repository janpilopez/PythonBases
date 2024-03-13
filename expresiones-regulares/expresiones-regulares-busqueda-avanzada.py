# Ahora podemos usar expresiones regulares para volver a resolver un ejercicio que
# hicimos antes, en el que nos interesaba la hora de cada email. En su momento,
# buscamos las líneas:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# con la intención de extraer la hora del día en cada línea. Antes logramos esto
# haciendo dos llamadas a split. Primero se dividía la línea en palabras y luego
# tomábamos la quinta palabra y la dividíamos de nuevo en el carácter “:” para
# obtener los dos caracteres que nos interesaban.

# Aunque esta solución funciona, es el resultado de código bastante frágil, que de-
# pende de asumir que las líneas tienen el formato adecuado. Si bien puedes agregar

# chequeos (o un gran bloque de try/except) para asegurarte que el programa no
# falle al encontrar líneas mal formateadas, esto hará que el programa aumente a 10
# o 15 líneas de código, que además serán difíciles de leer.
# Podemos lograr el resultado de forma mucho más simple utilizando la siguiente
# expresión regular:    
# ^From .* [0-9][0-9]:

# La traducción de esta expresión regular sería que estamos buscando líneas que
# empiecen con From (nótese el espacio), seguido de cualquier número de caracteres
# (.*), seguidos de un espacio en blanco, seguido de dos dígitos [0-9][0-9], seguidos
# de un carácter “:”. Esa es la definición de la clase de líneas que buscamos.
# Para extraer solo la hora usando findall(), agregamos paréntesis alrededor de
# los dos dígitos, de la siguiente manera:
# ^From .* ([0-9][0-9]):

# Búsqueda de líneas que comienzan con From y un caracter seguido
# de un número de dos dígitos entre 00 y 99 seguido de ':'
# Después imprimir el número si este es mayor a cero
import re
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 
for linea in man:
    linea = linea.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', linea)
    if len(x) > 0: print(x)
    
# Escapado de Caracteres
# Dado que en expresiones regulares usamos caracteres especiales para encontrar el
# comienzo o final de una línea o especificar comodines, necesitamos una forma de
# indicar que esos caracteres son “normales” y queremos encontrar la coincidencia
# con el carácter específico, como un “$” o “ˆ”.
# Podemos indicar que queremos encontrar la coincidencia con un carácter an-
# teponiéndole una barra invertida. Por ejemplo, podemos encontrar cantidades de
# dinero utilizando la siguiente expresión regular:
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x) #Especificamos que el caracter $ debe ser buscado , esto lo especificamos con la barra invertirda anteponiendolo
                    #si no puede dar el caso que lo tome como una expresion regular
print(y)
y = re.findall('[0-9.]+',x) #Si le quitamos el \ es nulo, y si le quitamos el dolar retorna una lista con las coincidencias
        #    ['10.00', '.']
                
# Dado que antepusimos la barra invertida al signo “$”, encuentra una coincidencia
# con el signo en la cadena en lugar de con el final de la línea, y el resto de la
# expresión regular coincide con uno o más dígitos del carácter “.” Nota: dentro de
# los corchetes, los caracteres no se consideran “especiales”. Por tanto, al escribir
# [0-9.], efectivamente significa dígitos o un punto. Cuando no está entre corchetes,
# el punto es el carácter “comodín” que coincide con cualquier carácter. Cuando está
# dentro de corchetes, un punto es un punto.


print('------------------------')
#Ejemplo con signo $ al final caracter $ expresion regular $
import re
x = 'We just received $10.00 for cookies'
y = re.findall(r's$', x) #Solo imprime la s si encuentra concidencia al final
# y = re.findall(r'a$', x) #No imprime nada porque no encuentra la a
print(y)


print('------------------------')

#EJEMPLO AMBICIOSO Y NO AMBICIOSO
#Por ejemplo, considera el siguiente patrón de expresión regular: [a*?b]
#Si se aplica a la cadena "aabab", la coincidencia para .*? será "aab", ya que es la secuencia más corta que satisface la expresión regular completa.
#Si usamos /a.*b/ en la misma cadena, la coincidencia para .* será "aabab", ya que es la secuencia más larga que satisface la expresión regular completa.
import re
x = 'aabab'
y = re.findall('a*?b', x) 
print(y) #['aab', 'ab']

print('------------------------')
import re
x = 'aabab'
y = re.findall('a?b', x) 
print(y) #['ab', 'ab']
