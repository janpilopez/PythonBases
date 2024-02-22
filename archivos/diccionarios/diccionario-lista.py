# Vamos a escribir un programa de Python para leer a través de las líneas del archivo,
# dividiendo cada línea en una lista de palabras, y después iterando a través de cada
# una de las palabras en la línea y contando cada palabra utilizando un diccionario.
# Verás que tenemos dos bucles for. El bucle externo está leyendo las líneas del
# archivo y el bucle interno está iterando a través de cada una de las palabras en
# esa línea en particular. Este es un ejemplo de un patrón llamado bucles anidados
# porque uno de los bucles es el bucle externo y el otro bucle es el bucle interno.
# Como el bucle interno ejecuta todas sus iteraciones cada vez que el bucle externo
# hace una sola iteración, consideramos que el bucle interno itera “más rápido” y el
# bucle externo itera más lento.
# La combinación de los dos bucles anidados asegura que contemos cada palabra en
# cada línea del archivo de entrada.
fname = input('Ingresa el nombre de archivo: ')
try:
    fhand = open(fname)
except:
    print('El archivo no se puede abrir:', fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)