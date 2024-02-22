a = 'banana'
b = 'banana'
# Por un lado, a y b se refieren a dos objetos diferentes que tienen el mismo valor.
# Por otro lado, apuntan al mismo objeto.
# Para revisar si dos variables apuntan al mismo objeto, puedes utilizar el operador is.
print(a is b)

# En este ejemplo, Python solamente creó un objeto de cadena, y ambos a y b
# apuntan a él.
# Pero cuando creas dos listas, obtienes dos objetos diferentes:
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
# False
# En este caso podríamos decir que las dos listas son equivalentes, porque tienen
# los mismos elementos, pero no idénticas, porque no son el mismo objeto. Si dos
# objetos son idénticos, son también equivalentes, pero si son equivalentes, no son
# necesariamente idénticos.

# Alias
# Si a se refiere a un objecto y tu asignasb = a, entonces ambas variables se refieren
# al mismo objeto:
a = [1, 2, 3]
b = a
print(b is a) #true

# La asociación de una variable a un objeto es llamada una referencia. En este
# ejemplo, hay dos referencias al mismo objeto.
# Un objeto con más de una referencia tiene más de un nombre, así que decimos que
# el objeto es un alias.
# Si el alias del objeto es mutable, los cambios hechos a un alias afectan al otro:
b[0] = 17
print(a)

# Aunque este comportamiento puede ser útil, es propenso a errores. En general, es
# más seguro evitar usar alias cuando estás trabajando con objetos mutables.
# Para objetos inmutables como cadenas, los alias no son un problema realmente.
# En este ejemplo:
a = 'banana'
b = 'banana'
# casi nunca hay diferencia si a y b apuntan a la misma cadena o no.


# Es importante distinguir entre operaciones que modifican listas y operaciones que
# crean nuevas listas. Por ejemplo, el método append modifica una lista, pero el
# operador + crea una nueva lista:
t1 = [1, 2]
t2 = t1.append(3)
print(t1)   
[1, 2, 3]
print(t2)
None

t3 = t1 + [3]
print(t3)
[1, 2, 3]
t2 is t3
False

# Esta diferencia es importante cuando escribes funciones que no están destinadas a
# modificar listas. Por ejemplo, esta función no elimina el primer elemento de una lista:
def mal_eliminar_primero(t):
    t = t[1:] # ¡EQUIVOCADO!
# El operador de rebanado crea una nueva lista y el asignamiento hace que t apunte
# a la lista, pero nada de esto tiene efecto en la lista que fue pasada como argumento.
# Una alternativa es escribir una función que cree y regrese una nueva lista. Por
# ejemplo, cola regresa todo excepto el primer elemento de una lista:
def cola(t):
    return t[1:]

letras = ['a', 'b', 'c']
resto = cola(letras)
print(resto)
print(letras) # Esta función deja la lista original sin modificar.

