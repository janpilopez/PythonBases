
# El operador + concatena listas:
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

[0] * 4
# =
[0, 0, 0, 0]

# Rebanado de listas
t = ['a', 'b', 'c', 'd', 'e', 'f']

print(t[1:4])
print(t[:4])
print(t[3:])

t = ['a', 'b', 'c', 'd', 'e', 'f']
# t[1:3] = ['x', 'y'] 3 hace referencia al segundo elemento nunca toma el ultimo
print(t)
# ['a', 'x', 'y', 'd', 'e', 'f']

# agregar un elemento al final
t = ['a', 'b', 'c']
t.append('d')

# extend toma una lista como argumento y agrega todos los elementos:
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
# Este ejemplo deja t2 sin modificar.
# ['a', 'b', 'c', 'd', 'e']

# sort ordena los elementos de la lista de menor a mayor:
t = ['d', 'c', 'e', 'b', 'a']
print(t)
# t.sort()
# print(t)
# ['a', 'b', 'c', 'd', 'e']

# La mayoría de métodos no regresan nada; modifican la lista y regresan None. Si
# accidentalmentes escribes t = t.sort(), vas a decepcionarte con el resultado.
t = t.sort()  #no es necesario asignacion solamente ejecutar el metodo
print(t)

# Eliminando elementos
# Hay varias formas de eliminar elementos de una lista. Si sabes el índice del elemento que quieres, puedes usar pop:
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)#elemento removido
# pop modifica la lista y regresa el elemento que fue removido. Si no provees un índice, la función elimina y retorna el último elemento.

# Si no necesitas el valor removido, puedes usar el operador del:
t = ['a', 'b', 'c']
del t[1]
print(t)

# Si sabes qué elemento quieres remover (pero no sabes el índice), puedes usar remove:
t = ['a', 'b', 'c']
t.remove('b')
print(t)
# ['a', 'c']

# Para remover más de un elemento, puedes usar del con un índice de rebanado:
t = ['a', 'b', 'c', 'd', 'e', 'f'] 
del t[1:5]#elimina del 1 al 4
print(t)
# ['a', 'f']
# Como siempre, el rebanado selecciona todos los elementos hasta, pero excluyendo, el segundo índice.