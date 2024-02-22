# Para escribir en un archivo, tienes que abrirlo en modo “w” (de write, escritura)
# como segundo parámetro:
fsal = open('salida.txt', 'w')
print(fsal)
# Si el archivo ya existía previamente, abrirlo en modo de escritura causará que se
# borre todo el contenido del archivo, así que ¡ten cuidado! Si el archivo no existe,
# un nuevo archivo es creado.

# El método write del manejador de archivos escribe datos dentro del archivo, de-
# volviendo el número de caracteres escritos. El modo de escritura por defecto es

# texto para escribir (y leer) cadenas.

linea2 = 'el símbolo de nuestra tierra.\n'
fsal.write(linea2)
fsal.close()
# Cuando terminas de escribir, tienes que cerrar el archivo para asegurarte que la
# última parte de los datos es escrita físicamente en el disco duro, de modo que no
# se pierdan los datos si la corriente eléctrica se interrumpe.

# Depuración

# Cuando estás leyendo y escribiendo archivos, puedes tener problemas con los es-
# pacios en blanco. Esos errores pueden ser difíciles de depurar debido a que los

# espacios, tabuladores, y saltos de línea son invisibles normalmente:
# >>> s = '1 2\t 3\n 4'
# >>> print(s)
# 1 2 3
# 4
# La función nativa repr puede ayudarte. Recibe cualquier objeto como argumento
# y devuelve una representación del objeto como una cadena. En el caso de las
# cadenas, representa los espacios en blanco con secuencias de barras invertidas:
# >>> print(repr(s))