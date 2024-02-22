# Bucles y diccionarios
# Si utilizas un diccionario como una secuencia para una sentencia for, esta recorre
# las claves del diccionario. Este bucle imprime cada clave y su valor correspondiente:
contadores = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for clave in contadores:
    print(clave, contadores[clave])

# si queremos encontrar todas las entradas en
# un diccionario con valor mayor a diez, podemos escribir el siguiente código:
for clave in contadores:
    if contadores[clave] > 10 :
        print(clave, contadores[clave])

# Si quieres imprimir las claves en orden alfabético, primero haces una lista de las
# claves en el diccionario utilizando el método keys disponible en los objetos de
# diccionario, y después ordenar esa lista e iterar a través de la lista ordenada, bus-
# cando cada clave e imprimiendo pares clave-valor ordenados, tal como se muestra
lst = list(contadores.keys()) 
print(lst)
lst.sort()
for clave in lst:
    print(clave, contadores[clave])

