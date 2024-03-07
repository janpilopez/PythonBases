manejador_archivo = open('C:/Users/jp/Documents/Python/archivos/mbox.txt')
print(manejador_archivo)
contador = 0
for linea in manejador_archivo:
    contador = contador + 1
    print(linea.upper())
print('Contador de líneas:', contador)
# Si el open es exitoso, el sistema operativo nos devuelve un manejador de archivo.

# El manejador de archivo no son los datos contenidos en el archivo, sino un “mane-
# jador” (handler) que podemos usar para leer los datos. Obtendrás un manejador

# de archivo si el archivo solicitado existe y si tienes los permisos apropiados para
# leerlo.

#SI EL ARCHIVO ES PEQUEÑO PODEMOS LEERLO CON READ, PERO  SI ES MUY GRANDE(NO CABE EN LA MEMORIA PRINCIPAL)
#HAY QUE LEERLO UTILIZANDO UN CICLO FOR O WHILE
manejador_archivo = open('C:/Users/jp/Documents/Python/archivos/mbox-short.txt')
print((manejador_archivo.read()))
# print(len(manejador_archivo.read()))
# print(len(manejador_archivo.read()))#la segunda vez carga cero, porque una vez leiodo vacia el contenido por completo


#Windows
man = open('C:/Users/jp/Documents/Python/archivos/mbox-short.txt')
#Linux
man = open('/home/jean/Documentos/python/PythonBases/archivos/mbox-short.txt') 

