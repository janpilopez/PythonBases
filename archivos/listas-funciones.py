# Listas y funciones
# Hay un cierto número funciones internas que pueden ser utilizadas en las listas que
# te permiten mirar rápidamente a través de una lista sin escribir tus propios bucles:
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

# La función sum() solamente funciona cuando los elementos de la lista son números.
# Las otras funciones (max(), len(), etc.) funcionan con listas de cadenas y otros
# tipos que pueden ser comparados entre sí.

# numlista = list()
# while (True):
    # inp = input('Ingresa un número: ')
    # if inp == 'fin': break
    # valor = float(inp)
    # numlista.append(valor)
# promedio = sum(numlista) / len(numlista)
# print('Promedio:', promedio)

# Listas y cadenas
# Una cadena es una secuencia de caracteres y una lista es una secuencia de valores,
# pero una lista de caracteres no es lo mismo que una cadena. Para convertir una
# cadena en una lista de caracteres, puedes usar list:
s = 'spam'
t = list(s)
print(t)
['s', 'p', 'a', 'm']

# La función list divide una cadena en letras individuales. Si quieres dividir una
# cadena en palabras, puedes utilizar el método split:
s = 'suspirando por los fiordos'
t = s.split()
print(t)
# ['suspirando', 'por', 'los', 'fiordos']
print(t[2])
# los


# Puedes llamar split con un argumento opcional llamado delimitador que especifica
# qué caracteres usar para delimitar las palabras. El siguiente ejemplo utiliza un
# guión medio como delimitador:
s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)
['spam', 'spam', 'spam']


# join es el inverso de split. Este toma una lista de cadenas y concatena los
# elementos. join es un método de cadenas, así que tienes que invocarlo en el
# delimitador y pasar la lista como un parámetro:
t = ['suspirando', 'por', 'los', 'fiordos']
delimiter = ' '
print(delimiter.join(t))
# 'suspirando por los/ fiordos'


#buscar elemento dentro de una lista
lista = [1, 50, 30]
if 50 in lista: # Imprime lo de abajo
    print("El número 50 existe en la lista")