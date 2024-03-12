# Los diccionarios tienen un método llamado items que retorna una lista de tuplas,
# donde cada tupla es un par clave-valor:
d = {'b':1, 'a':10, 'c':22}
t = (d.items()) #diccionario retorna diccionario lista de tuplas
print(t) #ES LO MISMO RETORNA UNA LISTA
t = list(d.items())
print(t) #diccionario-tupla retorna una lista de tuplas

# Como sería de esperar en un diccionario, los elementos no tienen ningún orden en
# particular.
# Aun así, puesto que la lista de tuplas es una lista, y las tuplas son comparables,
# ahora se puede ordenar la lista de tuplas. Convertir un diccionario en una lista de
# tuplas es una forma de obtener el contenido de un diccionario ordenado según sus
# claves:
t.sort()
print(t)
# La nueva lista está ordenada en orden alfabético ascendente de acuerdo al valor de
# sus claves.

# Asignación múltiple con diccionarios
# La combinación de items, asignación de tuplas, y for, produce un buen patrón de
# diseño de código para recorrer las claves y valores de un diccionario en un único bucle:
for clave, valor in list(d.items()):
    print(valor, clave)
# Este bucle tiene dos variables de iteración, debido a que items retorna una lista
# de tuplas y clave, valor es una asignación en tupla que itera sucesivamente a
# través de cada uno de los pares clave-valor del diccionario.
# Para cada iteración a través del bucle, tanto clave y valor van pasando al siguiente
# par clave-valor del diccionario (todavía en orden de dispersión).
    
# Si se combinan esas dos técnicas, se puede imprimir el contenido de un diccionario
# ordenado por el valor almacenado en cada par clave-valor.
    
d = {'a':10, 'b':1, 'c':22}
l = list()

for clave, valor in (d.items()) :
# for clave, valor in list(d.items()) : #da lo mismo
    l.append( (valor, clave) )

print(l)
l.sort(reverse=True) #ordenar de mayor a menor

print(l)