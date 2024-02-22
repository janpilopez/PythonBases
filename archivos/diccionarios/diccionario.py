# Un diccionario es como una lista, pero más general. En una lista, los índices de
# posiciones tienen que ser enteros; en un diccionario, los índices pueden ser (casi)
# cualquier tipo.
# Puedes pensar en un diccionario como una asociación entre un conjunto de índices
# (que son llamados claves) y un conjunto de valores. Cada clave apunta a un valor.
# La asociación de una clave y un valor es llamada par clave-valor o a veces elemento.
# Como ejemplo, vamos a construir un diccionario que asocia palabras de Inglés a
# Español, así que todas las claves y los valores son cadenas.
# La función dict crea un nuevo diccionario sin elementos. Debido a que dict es el
# nombre de una función interna, deberías evitar usarlo como un nombre de variable.
# La función dict crea un nuevo diccionario sin elementos. Debido a que dict es el
# nombre de una función interna, deberías evitar usarlo como un nombre de variable.
eng2sp = dict()
print(eng2sp)

# Las llaves, {}, representan un diccionario vacío. Para agregar elementos a un
# diccionario, puedes utilizar corchetes:
eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

# El orden de los pares clave-elemento no es el mismo. De hecho, si tu escribes este
# mismo ejemplo en tu computadora, podrías obtener un resultado diferente. En
# general, el orden de los elementos en un diccionario es impredecible.
# Pero ese no es un problema porque los elementos de un diccionario nunca son
# indexados con índices enteros. En vez de eso, utilizas las claves para encontrar los
# valores correspondientes:
print(eng2sp['two'])

# La función len funciona en diccionarios; ésta regresa el número de pares clave-
# valor:
print(len(eng2sp))

# El operador in funciona en diccionarios; éste te dice si algo aparece como una clave
# en el diccionario (aparecer como valor no es suficiente).
print('one' in eng2sp)

print('uno' in eng2sp)

# Para ver si algo aparece como valor en un diccionario, puedes usar el método
# values, el cual retorna los valores como una lista, y después puedes usar el operador in:
vals = list(eng2sp.values())
print('uno' in vals)

# El operador in utiliza diferentes algoritmos para listas y diccionarios. Para listas,
# utiliza un algoritmo de búsqueda lineal. Conforme la lista se vuelve más grande, el
# tiempo de búsqueda se vuelve más largo en proporción al tamaño de la lista. Para
# diccionarios, Python utiliza un algoritmo llamado tabla hash (hash table, en inglés)
#se busuca por clave no por valor.
# 9.1. DICCIONARIO COMO UN CONJUNTO DE CONTADORES 115
# que tiene una propiedad importante: el operador in toma la misma cantidad de
# tiempo sin importar cuántos elementos haya en el diccionario.

def contar_letras(cadena):
    contador_letras = [0] * 26  # Crear una lista con 26 elementos inicializados en 0

    for caracter in cadena:
        indice = ord(caracter) - ord('a')  # Convertir el carácter en un índice
        print(indice, ord(caracter), ord('a'), 'eke,[lp]')
        contador_letras[indice] += 1

    # Imprimir los resultados
    for i in range(26):
        letra = chr(i + ord('a'))  # Obtener la letra correspondiente al índice
        print("Cantidad de veces que aparece la letra", letra + ":", contador_letras[i])
contar_letras('ccccggsfgettttt')

# CON DICCIONARIO QUEDARIA ASI
palabra = 'brontosaurio'
d = dict()
for c in palabra:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)


# Los diccionarios tienen un método llamado get que toma una clave y un valor por
# defecto. Si la clave aparece en el diccionario, get regresa el valor correspondiente;
# si no, regresa el valor por defecto. Por ejemplo:
cuentas = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(cuentas.get('jan', 0))
print(cuentas.get('tim',0))

# Podemos usar get para escribir nuestro bucle de histograma más conciso. Puesto
# que el método get automáticamente maneja el caso en que una clave no está en el
# diccionario, podemos reducir cuatro líneas a una y eliminar la sentencia if.
#histograma es como un historial o un par-clave que sea usa con los diccionarios {'b': 1, 'r': 2, 'o': 3, 'n': 1, 't': 1, 's': 1, 'a': 1, 'u': 1, 'i': 1}
palabra = 'brontosaurio'
d = dict()
for c in palabra:
    d[c] = d.get(c,0) + 1#/SI NO EXISTE RETORNA 0(este valor es el argumento se asigna por defecto sea que exista o no) y se le suma 1, si existe retorna el valor y se le suma 1
print(d)