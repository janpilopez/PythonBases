# Depuración
# El uso descuidado de listas (y otros objetos mutables) puede llevar a largas horas
# de depuración. Aquí están algumos de los errores más comunes y las formas de evitarlos:
# 1. No olvides que la mayoría de métodos de listas modifican el argumento y
# regresan None. Esto es lo opuesto a los métodos de cadenas, que regresan
# una nueva cadena y dejan la original sin modificar.
# Si estás acostumbrado a escribir código de cadenas como este:
palabra = 'hola '
palabra = palabra.strip()
# Estás propenso a escribir código de listas como este:
t = [8, 2,4]
t = t.sort() # ¡EQUIVOCADO! devielve none 
print(t)
t = [8, 2,4]
t.sort()
print(t)
# Debido a que sort regresa None, la siguiente operación que hagas con t es
# probable que falle.
# Antes de usar métodos y operadores de listas, deberías leer la documentación
# cuidadosamente y después probarlos en modo interactivo.



# Elige un estilo y apégate a él.
# Parte del problema con listas es que hay demasiadas formas de hacer las
# cosas. Por ejemplo, para remover un elemento de una lista, puedes utilizar
# pop, remove, del, o incluso una asignación por rebanado.
# Para agregar un elemento, puedes utilizar el método append o el operador +.
# Pero no olvides que esos también son correctos:
x=5
t.append(x)
# print(t)
t = t + [x]
# print(t)
x=7


# Y esos son incorrectos:
t.append([x]) # ¡EQUIVOCADO!
# t = t.append(x) # ¡EQUIVOCADO!
# t + [x] # ¡EQUIVOCADO!
# t = t + x # ¡EQUIVOCADO!
# print(t)


#DEPURACION
# Hacer copias para evitar alias.
# Si quieres utilizar un método como sort que modifica el argumento, pero
# necesitas mantener la lista original también, puedes hacer una copia.
t = [8, 2,4]
orig = t[:]
t.sort()
print(t)

# En este ejemplo podrías tambien usar la función interna sorted, la cual
# regresa una lista nueva y ordenada, y deja la original sin modificar. ¡Pero en
# ese caso deberías evitar usar sorted como un nombre de variable!
t = [8, 2,4]
x = sorted(t)
print(x)
print('ORIGINAL T:', t)