import string
manejador = open('C:/Users/jp/Documents/Python/archivos/romeo-full.txt')

contadores = dict()
for linea in manejador:
    linea = linea.translate(str.maketrans('', '', string.punctuation)) #quitamos las puntiaciones y asignamos con translate
    linea = linea.lower()
    palabras = linea.split()
    for palabra in palabras:
        if palabra not in contadores:
            contadores[palabra] = 1
        else:
            contadores[palabra] += 1
# Ordenar el diccionario por valor
lst = list()
for clave, valor in list(contadores.items()):
    lst.append((valor, clave))
lst.sort(reverse=True)
# Si hay más de una tupla con el mismo valor, se tendrá en cuenta el segundo elemento (la
# clave), de forma que las tuplas cuyo valor es el mismo serán también ordenadas en orden alfabético según su clave.
for clave, valor in lst[:10]: #solo imprimos los 10 primeros valores
    print(clave, valor)