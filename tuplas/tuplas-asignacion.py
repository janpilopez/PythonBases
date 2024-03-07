# Asignación de tuplas
# Una de las características sintácticas únicas del lenguaje Python es la capacidad de
# tener una tupla en el lado izquierdo de una sentencia de asignación. Esto permite
# asignar más de una variable a la vez cuando hay una secuencia del lado izquierdo.
# En este ejemplo tenemos una lista de dos elementos (la cual es una secuencia) y
# asignamos el primer y segundo elementos de la secuencia a las variables x y y en
# una única sentencia.
m = [ 'pásalo', 'bien' ]
x, y = m #asignamos pasalo al primer elementos x  ~~¡¡¡~~~  asignamos bien al segundo elemento y
# (x,y)
print(x)
print(y)
# Python no traduce la sintaxis literalmente. Por ejemplo, si se trata de hacer esto con un
# diccionario, no va a funcionar como se podría esperar.
# No es magia, Python traduce aproximadamente la sintaxis de asignación de la
# tupla de este modo

m = [ 'pásalo', 'bien' ]
x = m[0]
y = m[1]

# Estilísticamente, cuando se utiliza una tupla en el lado izquierdo de la asignación,
# se omiten los paréntesis, pero lo que se muestra a continuación es una sintaxis
# igualmente válida:
m = [ 'pásalo', 'bien' ]
(x, y) = m

# Una aplicación particularmente ingeniosa de asignación con tuplas permite inter-
# cambiar los valores de dos variables en una sola sentencia:
#       a, b = b, a

# Ambos lados de la sentencia son tuplas, pero el lado izquierdo es una tupla de
# variables; el lado derecho es una tupla de expresiones. Cada valor en el lado derecho
# es asignado a su respectiva variable en el lado izquierdo. Todas las expresiones en
# el lado derecho son evaluadas antes de realizar cualquier asignación.
# El número de variables en el lado izquierdo y el número de valores en el lado
# derecho deben ser iguales:
# >>> a, b = 1, 2, 3
# ValueError: too many values to unpack

# Generalizando más, el lado derecho puede ser cualquier tipo de secuencia (cadena,
# lista, o tupla). Por ejemplo, para dividir una dirección de e-mail en nombre de
# usuario y dominio, se podría escribir:
dir = 'monty@python.org'

nombreus, dominio = dir.split('@') #por eso es que dice que todas lex expresiones del lado derecho son evaluadas antes de ser asignadas
#aqui se crea un lista con dos elementos, ek nombre y el dominio

# El valor de retorno de split es una lista con dos elementos; el primer elemento es
# asignado a nombre, el segundo a dominio.
print(nombreus)
# monty
print(dominio)
# python.org