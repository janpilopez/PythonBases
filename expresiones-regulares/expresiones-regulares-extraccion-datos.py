# Extrayendo datos usando expresiones regulares
import re
s = 'Una nota de csev@umich.edu a cwen@iupui.edu sobre una reunión @2PM'
lst = re.findall(r'\S+@\S+', s)
print(lst)
# El método findall() busca en la cadena en el segundo argumento y retorna una
# lista de todas las cadenas que parecen ser direcciones de email. Estamos usando
# una secuencia de dos caracteres que coincide con un carácter distinto a un espacio
# en blanco (\S). SIGNIFICA QUE \S es cualquier caracter que no sea un espacio en blanco

# Traduciendo la expresión regular al castellano, estamos buscando subcadenas que
# tengan al menos un carácter que no sea un espacio, seguido de una @, seguido de al
# menos un carácter que no sea un espacio. La expresión \S+ coincidirá con cuantos
# caracteres distintos de un espacio sea posible.

# Búsqueda de líneas que tengan una arroba entre caracteres
import re
# man = open('mbox-short.txt')
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 

for linea in man:
    linea = linea.rstrip()
    x = re.findall(r'\S+@\S+', linea)
    if len(x) > 0:
        print(x)

# Con esto, leemos cada línea y luego extraemos las subcadenas que coincidan con
# nuestra expresión regular. Dado que findall() retorna una lista, simplemente
# revisamos si el número de elementos en ésta es mayor a cero e imprimir solo líneas
# donde encontramos al menos una subcadena que pudiera ser una dirección de email.

# Algunas de las direcciones tienen caracteres incorrectos como “<” o “;” al comienzo
# o al final. Declaremos que solo estamos interesados en la parte de la cadena que
# comience y termine con una letra o un número.
# Para lograr esto, usamos otra característica de las expresiones regulares. Los
# corchetes se usan para indicar un conjunto de caracteres que queremos aceptar
# como coincidencias. La secuencia \S retornará el conjunto de “caracteres que no
# sean un espacio en blanco”. Ahora seremos un poco más explícitos en cuanto a los
# caracteres respecto de los cuales buscamos coincidencias.
# Esta será nuestra nueva expresión regular:

# [a-zA-Z0-9]\S*@\S*[a-zA-Z]
print('***************************************************************************')

# Búsqueda de líneas que tengan una arroba entre caracteres
# Los caracteres deben ser una letra o un número
import re
#Esto significa que la cadena se tomara como arriba pero al encontrar antes o despues de @ algun caracter no lo tomará en cuenta
#es lo mismo de arriba pero la diferencia que arriba corta la subcadena cuando encuentra un espacio en blanco de la cadena principal
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 
for linea in man:
    linea = linea.rstrip()
    x = re.findall(r'[a-zA-Z0-9]\S+@\S+[a-zA-Z]', linea)
    if len(x) > 0:
        print(x)
        
# Nótese que en las líneas donde aparece source@collab.sakaiproject.org, nues-
# tra expresión regular eliminó dos caracteres al final de la cadena (“>;”). Esto
# se debe a que, cuando agregamos [a-zA-Z] al final de nuestra expresión regular,
# estamos determinando que cualquier cadena que la expresión regular encuentre al
# analizar el texto debe terminar con una letra. Por lo tanto, cuando vea el “>”
# al final de “sakaiproject.org>;”, simplemente se detiene en el último carácter que
# haya encontrado que coincida con ese criterio (en este caso, la “g” fue la última coincidencia).
# Nótese también que el resultado de la ejecución del programa es una lista de Python
# que tiene una cadena como su único elemento.