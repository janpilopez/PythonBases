# Glosario
# comparable Un tipo en el cual un valor puede ser revisado para ver si es mayor
# que, menor que, o igual a otro valor del mismo tipo. Los tipos que son
# comparables pueden ser puestos en una lista y ordenados.

# estructura de datos Una collección de valores relacionados, normalmente orga-
# nizados en listas, diccionarios, tuplas, etc.

# DSU Abreviatura de “decorate-sort-undecorate (decorar-ordenar-quitar la deco-
# ración)”, un patrón de diseño que implica construir una lista de tuplas, or-
# denarlas, y extraer parte del resultado.

# reunir La operación de tratar una secuencia como una lista de argumentos.
# hashable (dispersable) Un tipo que tiene una función de dispersión. Los tipos
# inmutables, como enteros, flotantes y cadenas son dispersables (hashables);
# los tipos mutables como listas y diccionarios no lo son.
# dispersar La operación de tratar una secuencia como una lista de argumentos.
# modelado (de una estructura de datos) Un resumen del tipo, tamaño, y
# composición de una estructura de datos.
# singleton Una lista (u otra secuencia) con un único elemento.
# tupla Una secuencia inmutable de elementos.
# asignación por tuplas Una asignación con una secuencia en el lado derecho y
# una tupla de variables en el izquierdo. El lado derecho es evaluado y luego
# sus elementos son asignados a las variables en el lado izquierdo.

# DSU
# Decorate (Decora) una secuencia, construyendo una lista de tuplas con uno o
# más índices ordenados precediendo los elementos de la secuencia,
# Sort (Ordena) la lista de tuplas utilizando la función interna sort, y
# Undecorate (Quita la decoración) extrayendo los elementos ordenados de la
# secuencia.
# Por ejemplo, suponiendo una lista de palabras que se quieren ordenar de la más
# larga a la más corta:
# txt = 'Pero qué luz se deja ver allí'
# palabras = txt.split()
# t = list()
# for palabra in palabras:
# t.append((len(palabra), palabra))
# t.sort(reverse=True)
# res = list()
# for longitud, palabra in t:
# res.append(palabra)
# print(res)
# # Código: https://es.py4e.com/code3/soft.py

# El primer bucle genera una lista de tuplas, donde cada tupla es una palabra pre-
# cedida por su longitud.

# sort compara el primer elemento (longitud) primero, y solamente considera el
# segundo elemento para desempatar. El argumento clave reverse=True indica a
# sort que debe ir en orden decreciente.
# El segundo bucle recorre la lista de tuplas y construye una lista de palabras en
# orden descendente según la longitud. Las palabras de cuatro letras están ordenadas
# en orden alfabético inverso, así que “deja” aparece antes que “allí” en la siguiente
# lista.
# La salida del programa es la siguiente:
# ['deja', 'allí', 'Pero', 'ver', 'qué', 'luz', 'se']