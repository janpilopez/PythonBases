# Las Tuplas son inmutables
# Una tupla1

# es una secuencia de valores similar a una lista. Los valores guardados
# en una tupla pueden ser de cualquier tipo, y son indexados por números enteros.
# La principal diferencia es que las tuplas son inmutables. Las tuplas además son
# comparables y dispersables (hashables) de modo que las listas de tuplas se pueden
# ordenar y también usar tuplas como valores para las claves en diccionarios de
# Python.
# Sintácticamente, una tupla es una lista de valores separados por comas:
t = 'a', 'b', 'c', 'd', 'e'
print(t)
# Aunque no es necesario, es común encerrar las tuplas entre paréntesis para ayu-
# darnos a identificarlas rápidamente cuando revisemos código de Python:

t = ('a', 'b', 'c', 'd', 'e')
print(t)

# Para crear una tupla con un solo elemento, es necesario incluir una coma al final:
t1 = ('a',)
print(type(t1))
# Sin la coma, Python considera ('a') como una expresión con una cadena entre paréntesis que es evaluada como de tipo cadena (string):

# Otra forma de construir una tupla es utilizando la función interna tuple. Sin
# argumentos, ésta crea una tupla vacía:
t = tuple()
print(t)

# Si el argumento es una secuencia (cadena, lista, o tupla), el resultado de la llamada
# a tuple es una tupla con los elementos de la secuencia:
t = tuple('altramuces')
print(t)

# La mayoría de los operadores de listas también funcionan en tuplas. El operador
# corchete indexa un elemento:
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])

# Y el operador de rebanado (slice) selecciona un rango de elementos.
print(t[1:3])

# Pero si se intenta modificar uno de los elementos de la tupla, se produce un error:
# t[0] = 'A' # TypeError: object doesn't support item assignment

# No se puede modificar los elementos de una tupla, pero sí se puede reemplazar una
# tupla por otra:
t = ('A',) + t[1:] #crear un nuevo elemento A, y le agrega la t que va desde el index 1 al ultimo
print("tupla reemplazada",t)
