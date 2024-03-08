# Expresiones regulares
# Python tiene una librería muy
# poderosa llamada expresiones regulares que maneja varias de estas tareas de man-
# era bastante elegante. La razón por la que no presentamos las expresiones regulares
# antes se debe a que, aunque son muy poderosas, son un poco más complicadas y
# toma algo de tiempo acostumbrarse a su sintaxis.

# + = 1 o mas veces
# * = o o mas veces

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
print(' -----------**********************----------- ')

# Ahora solo retornará líneas que comiencen con la cadena “From:”. Este sigue siendo
# un ejemplo muy sencillo que podríamos haber implementado usando el método
# startswith() de la librería de cadenas. Pero sirve para presentar la idea de que
# las expresiones regulares contienen caracteres especiales que nos dan mayor control
# sobre qué coincidencias retornará la expresión regular.

# Coincidencia de caracteres en expresiones regulares
# Existen varios caracteres especiales que nos permiten construir expresiones regu-
# lares incluso más poderosas. 
# El más común es el punto, que coincide con cualquier carácter.
# En el siguiente ejemplo, la expresión regular F..m: coincidiría con las cadenas
# “From:”, “Fxxm:”, “F12m:”, o “F!@m:”, ya que los caracteres de punto en la
# expresión regular coinciden con cualquier carácter.
# # Búsqueda de líneas que comiencen con 'F', seguidas de
# 2 caracteres, seguidos de 'm:'
import re
# man = open('mbox-short.txt')
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 
for linea in man:
    linea = linea.rstrip()
    if re.search('^F..m:', linea): #Muestra cualquier linea que empieze con F..m (el . es cualquier caracter o letra intermedia)
        print(linea)

# Esto resulta particularmente poderoso cuando se le combina con la habilidad de
# indicar que un carácter puede repetirse cualquier cantidad de veces usando los
# caracteres * o + en tu expresión regular. Estos caracteres especiales indican que
# en lugar de coincidir con un solo carácter en la cadena de búsqueda, coinciden con
# cero o más caracteres (en el caso del asterisco) o con uno o más caracteres (en el
# caso del signo de suma).
# Podemos reducir más las líneas que coincidan usando un carácter comodín en el
# siguiente ejemplo:
# Búsqueda de líneas que comienzan con From y tienen una arroba
print(' -------.+@---------------- ')
import re
#Recordar que siempre que se lee un documento este es vaciado por lo que siempre lo volvemos a cargar
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 
for linea in man:
    linea = linea.rstrip()
    if re.search('^From:.+k', linea): #con esto especificamos que la linea debe empezar con From 
        #y tener cualquier caracter o letra intermedia y terminar con k (cualquier cosa que lleve k) aparecerá
        print(linea)
        
# La cadena ˆFrom:.+@ retornará coincidencias con líneas que empiecen con “From:”,
# seguidas de uno o más caracteres (.+), seguidas de un carácter @. Por lo tanto, la
# siguiente línea coincidirá:
# From: stephen.marquard@uct.ac.za
# Puede considerarse que el comodín .+ se expande para abarcar todos los caracteres
# entre los signos : y @.
# From:.+@
# Conviene considerar que los signos de suma y los asteriscos “empujan”. Por ejemplo,
# la siguiente cadena marcaría una coincidencia con el último signo @, ya que el .+
# “empujan” hacia afuera, como se muestra a continuación:
# From: stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @iupui.edu
# Es posible indicar a un asterisco o signo de suma que no debe ser tan “ambicioso”
# agregando otro carácter. Revisa la documentación para obtener información sobre
# cómo desactivar este comportamiento ambicioso.