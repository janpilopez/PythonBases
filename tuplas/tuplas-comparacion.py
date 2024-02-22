# Comparación de tuplas
# Los operadores de comparación funcionan con tuplas y otras secuencias. Python
# comienza comparando el primer elemento de cada secuencia. Si ambos elementos
# son iguales, pasa al siguiente elemento y así sucesivamente, hasta que encuentra
# elementos diferentes. Los elementos subsecuentes no son considerados (aunque
# sean muy grandes).

print((0, 1, 2) < (0, 3, 4))
# True
print((1, 100, 2000000) < (5, 3, 4)) #Automaticamente al encontrar diferencia en el segundo elemento (100,3) vota false no sigue el ciclo 
# por lo que corta es algo por el guardian
# False

# La función sort funciona de la misma manera. Ordena inicialmente por el primer
# elemento, pero en el caso de que ambos elementos sean iguales, ordena por el
# segundo elemento, y así sucesivamente.
# Esta característica se presta a un patrón de diseño llamado DSU, que
# Decorate (Decora) una secuencia, construyendo una lista de tuplas con uno o
# más índices ordenados precediendo los elementos de la secuencia,
# Sort (Ordena) la lista de tuplas utilizando la función interna sort, y
# Undecorate (Quita la decoración) extrayendo los elementos ordenados de la
# secuencia.

txt = 'Pero qué luz se deja ver allí'
palabras = txt.split()
t = list()
for palabra in palabras:
    t.append((len(palabra), palabra))#guardaron tuplas en una lista (len,palabra)
    t.sort(reverse=True) #ordena la lista t en orden descendente según el primer elemento de cada tupla, es decir, la longitud de la palabra.
res = list()
for ola, palabra in t: #aqui se utiliza dos parametrros ya que en cada elementos hay una tupla tambien podria ser (a,b) in t
    # print(longitud, palabra) 
    res.append(palabra)
print(res)