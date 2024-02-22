quesos = ['Cheddar', 'Edam', 'Gouda']
numeros = [17, 123]
vacia = []
print(quesos, numeros, vacia)

# A diferencia de las cadenas, las listas son mutables porque pueden cambiar el
# orden de los elementos en una lista o reasignar un elemento en una lista. Cuando
# el operador corchete aparece en el lado izquierdo de una asignación, éste identifica
# el elemento de la lista que será asignado.
numeros = [17, 123]
numeros[1] = 5
print(numeros)

# El operador in funciona también en listas.
quesos = ['Cheddar', 'Edam', 'Gouda']
print('Edam' in quesos)

for queso in quesos:
    print(queso)

# Esto funciona bien si solamente necesitas leer los elementos de la lista. Pero si
# quieres escribir o actualizar los elementos, necesitas los índices. Una forma común
# de hacer eso es combinando las funciones range y len:
for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2

# Este bucle recorre la lista y actualiza cada elemento. len regresa el número de
# elementos en una lista. range regresa una lista de índices desde 0 hasta n − 1,
# donde n es la longitud de la lista. Cada vez que pasa a través del recorrido, i
# obtiene el índice del siguiente elemento. La sentencia de asignación dentro del
# bucle utiliza