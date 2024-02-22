#El operador de formato % nos permite construir cadenas, reemplazando partes de
#las cadenas con datos almacenados en variables. Cuando lo aplicamos a enteros, %
#es el operador módulo. Pero cuando es aplicado a una cadena, % es el operador de
#formato.
camellos = 42
#lo usamos para concatenar variables en cadenas
print('%d' % camellos)
# d es decimal
camellos = 42
print('Yo he visto %d camellos.' % camellos)