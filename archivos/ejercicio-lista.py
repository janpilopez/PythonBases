manejador_archivo = open('C:/Users/jp/Documents/Python/archivos/romeo.txt')
lista = []
for linea in manejador_archivo:
    palabra = linea.split()
    for elemento in palabra:
        if not elemento in lista: lista.append(elemento)

lista.sort()
print(lista)