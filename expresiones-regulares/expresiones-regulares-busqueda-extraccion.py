# Combinando búsqueda y extracción
# Si quisiéramos encontrar los números en las líneas que empiecen con la cadena “X-”, como por ejemplo:
# X-DSPAM-Confidence: 0.8475
# X-DSPAM-Probability: 0.0000
# no queremos cualquier número de coma flotante contenidos en cualquier línea. Solo
# queremos extraer los números de las líneas que tienen la sintaxis ya mencionada.
# Podemos construir la siguiente expresión regular para seleccionar las líneas:
# ^X-.*: [0-9.]+
#Significa que busque la coincidencias que empiezen con X- (cualquier cosa) seguido de : (valor) \\ con esto filtramos al final para obtener cadenas que tengas valores
# [ 0-9. ] significa que puede ser cualquier cosa que empieze cobn un numero(decimal,entero ,flotante),o punto


# Traduciendo esto, estamos diciendo que queremos líneas que empiecen con X-,
# seguido por cero o más caracteres (.*), seguido por un carácter de dos puntos
# (:) y luego un espacio. Después del espacio, buscamos uno o más caracteres que
# sean, o bien un dígito (0-9), o bien un punto [0-9.]+. Nótese que al interior de
# los corchetes el punto efectivamente corresponde a un punto (es decir, no funciona
# como comodín entre corchetes).
# La siguiente es una expresión bastante comprimida que solo retornará las líneas
# que nos interesan:
import re
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 
for linea in man:
    linea = linea.rstrip()
    if re.search(r'^X\S*: [0-9.]+', linea):
    # if re.search(r'^X-\S*: [0-9.]+', linea): //Con guion tambien es valido sino solo que empieze con X como arriba
    # ^X-.*: [0-9.]+ o incluso podemos ubicar esta expresion pero la de arriba es mas comprimida
        print(linea)
        
# Búsqueda de líneas que comiencen con 'X' seguida de cualquier caracter (* con cero o mas coincidencias) que
# no sea espacio y ':' seguido de un espacio y cualquier número.
# El número incluye decimales.

# Ahora, debemos resolver el problema de extraer los númueros. Aunque sería bas-
# tante sencillo usar split, podemos echar mano a otra función de las expresiones
# regulares para buscar y analizar la línea a la vez.

# Los paréntesis son otros caracteres especiales en las expresiones regulares. Al agre-
# gar paréntesis a una expresión regular, son ignorados a la hora de hacer coincidir
# la cadena (por ejemplo (0,3) no toma estos valores solo los que estan dentor de ese rango). 
# Pero cuando se usa findall(), los paréntesis indican que, aunque se
# quiere que toda la expresión coincida, solo interesa extraer una parte de la subca-
# dena que coincida con la expresión regular.
# Entonces, hacemos los siguientes cambios a nuestro programa:

# Búsqueda de líneas que comiencen con 'X' seguida de cualquier caracter que
# no sea espacio en blanco y ':' seguido de un espacio y un número.
# El número puede incluir decimales.
# Después imprimir el número si es mayor a cero.
import re
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 
for linea in man:
    linea = linea.rstrip()
    x = re.findall(r'^X\S*: ([0-9.]+)', linea) #Los parentesis indican solo lo que quiero mostrar
    if len(x) > 0:
        print(x)
# En lugar de usar search(), agregamos paréntesis alrededos de la parte de la ex-
# presión regular que representa al número de coma flotante para indicar que solo
# queremos que findall() retorne la parte correspondiente a números de coma
# flotante de la cadena retornada.
# El resultado de este programa es el siguiente:
# ['0.8475']

# Los números siguen estando en una lista y deben ser convertidos de cadenas a
# números de coma flotante, pero hemos usado las expresiones regulares para buscar
# y extraer la información que consideramos interesante.
# Otro ejemplo de esta técnica: si revisan este archivo, verán una serie de líneas en
# el formulario:
# Detalles: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772


# Si quisiéramos extraer todos los números de revisión (el número entero al final de
# esas líneas) usando la misma técnica del ejemplo anterior, podríamos escribir el
# siguiente programa:
# Búsqueda de líneas que comiencen con 'Details: rev='
# seguido de números y '.'
# Después imprimir el número si es mayor a cero
import re
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 
for linea in man:
    linea = linea.rstrip()
    # Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
    x = re.findall('^Details:.*rev=([0-9.]+)', linea) #Si le quitamos el punto no trae decimales
                                        # + [no se le especifica ningun caracter] puede ir cualquier cosa despues
    if len(x) > 0:
        print(x)
        
# Recuerda que la expresión [0-9]+ es “ambiciosa” e intentará formar una cadena de
# dígitos lo más larga posible antes de extraerlos. Este comportamiento “ambicioso”
# es la razón por la que obtenemos los cinco dígitos de cada número. La expresiones
# regular se expande en ambas direcciones hasta que encuentra, o bien un carácter
# que no sea un dígito, o bien el comienzo o final de una línea.
# Ahora podemos usar expresiones regulares para volver a resolver un ejercicio que
# hicimos antes, en el que nos interesaba la hora de cada email. En su momento,
# buscamos las líneas: