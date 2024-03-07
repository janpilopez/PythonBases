# Uso de tuplas como claves en diccionarios
# Dado que las tuplas son dispersables (hashable) y las listas no, si se quiere crear
# una clave compuesta para usar en un diccionario, se debe utilizar una tupla como
# clave.
# Usaríamos por ejemplo una clave compuesta si quisiéramos crear un directorio
# telefónico que mapea pares appellido, nombre con números telefónicos. Asumiendo
# que hemos definido las variables apellido, nombre, y número, podríamos escribir
# una sentencia de asignación de diccionario como sigue:
# directorio[apellido,nombre] = numero
directorio = dict()

directorio['Smith', 'John'] = 1234567

# La expresión entre corchetes es una tupla. Podríamos utilizar asignación de tuplas
# en un bucle for para recorrer este diccionario.
for apellido, nombre in directorio:
    print(nombre, apellido, directorio[apellido,nombre])

# elementos de cada tupla a apellido y nombre, después imprime el nombre y el
# número telefónico correspondiente.


# Me he enfocado en listas de tuplas, pero casi todos los ejemplos de este capítulo
# funcionan también con listas de listas, tuplas de tuplas, y tuplas de listas. Para
# evitar enumerar todas las combinaciones posibles, a veces es más sencillo hablar
# de secuencias de secuencias.
# En muchos contextos, los diferentes tipos de secuencias (cadenas, listas, y tuplas)
# pueden intercambiarse. Así que, ¿cómo y por qué elegir uno u otro?

# Para comenzar con lo más obvio, las cadenas están más limitadas que otras secuen-
# cias, debido a que los elementos tienen que ser caracteres. Además, son inmutables.

# Si necesitas la capacidad de cambiar los caracteres en una cadena (en vez de crear
# una nueva), quizá prefieras utilizar una lista de caracteres.
# Las listas son más comunes que las tuplas, principalmente porque son mutables.
# Pero hay algunos casos donde es preferible utilizar tuplas:
# 1. En algunos contextos, como una sentencia return, resulta sintácticamente
# más simple crear una tupla que una lista. En otros contextos, es posible que
# prefieras una lista.
# 2. Si quieres utilizar una secuencia como una clave en un diccionario, debes usar
# un tipo inmutable como una tupla o una cadena.
# 3. Si estás pasando una secuencia como argumento de una función, el uso de
# tuplas reduce la posibilidad de comportamientos inesperados debido a la
# creación de alias.

# Dado que las tuplas son inmutables, no proporcionan métodos como sort y
# reverse, que modifican listas ya existentes. Sin embargo, Python proporciona las
# funciones internas sorted y reversed, que toman una secuencia como parámetro
# y devuelven una secuencia nueva con los mismos elementos en un orden diferente.


# 10.9 Depuración
# Las listas, diccionarios y tuplas son conocidas de forma genérica como estructuras
# de datos; en este capítulo estamos comenzando a ver estructuras de datos compues-
# tas, como listas de tuplas, y diccionarios que contienen tuplas como claves y listas
# como valores. Las estructuras de datos compuestas son útiles, pero también son
# propensas a lo que yo llamo errores de modelado; es decir, errores causados cuando
# una estructura de datos tiene el tipo, tamaño o composición incorrecto, o quizás
# al escribir una parte del código se nos olvidó cómo era el modelado de los datos
# y se introdujo un error. Por ejemplo, si estás esperando una lista con un entero y
# recibes un entero solamente (no en una lista), no funcionará.