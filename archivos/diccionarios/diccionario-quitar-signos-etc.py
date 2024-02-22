#QUITAR SIGOS DE PUNTUACION Y CONVIRTIENDO TODO EN UN SOLO FORMATO
# Podemos resolver ambos problemas utilizando los métodos de cadenas lower,
# punctuation, y translate. El método translate es el más sutil de los métodos.
# Aquí esta la documentación para translate:
# line.translate(str.maketrans(fromstr, tostr, deletestr))
# Reemplaza los caracteres en fromstr con el caracter en la misma posición en tostr
# y elimina todos los caracteres que están en deletestr. Los parámetros fromstr y
# tostr pueden ser cadenas vacías y el parámetro deletestr es opcional.
import string
print(string.punctuation) # es un string predefinido en el módulo string que contiene todos los caracteres de puntuación comunes, como signos de interrogación, comas, puntos, etc

manejador_archivo = open('C:/Users/jp/Documents/Python/archivos/romeo.txt')
counts = dict()
for line in manejador_archivo:
    line = line.rstrip() #elimina espacios en blanco al final de cada linea
    line = line.translate(line.maketrans('', '', string.punctuation)) #elimina todos los caracteres de puntuacion de cada linea
    line = line.lower() #letras en minusculas
    words = line.split() #array
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)

# La función maketrans() crea una tabla de traducción que se utiliza para especificar cómo se deben mapear los caracteres en una cadena. Acepta tres argumentos: cadena_de_entrada, cadena_de_salida y cadena_de_caracteres_a_eliminar
# En este caso particular, estamos utilizando maketrans('', '', string.punctuation). Aquí hay una explicación más detallada de cada argumento
# El primer argumento, cadena_de_entrada, se establece en '' (una cadena vacía). Esto significa que no hay caracteres de entrada que se traducirán a otros caracteres. En otras palabras, no se realizará ninguna sustitución de caracteres
# El segundo argumento, cadena_de_salida, también se establece en '' (una cadena vacía). Esto significa que no hay caracteres de salida especificados. No se realizará ninguna traducción de caracteres
# El tercer argumento, cadena_de_caracteres_a_eliminar, se establece en string.punctuation. string.punctuation es una constante predefinida en el módulo string que contiene todos los caracteres de puntuación comunes, como signos de interrogación, comas, puntos, etc. Al pasar string.punctuation como tercer argumento, estamos indicando que queremos eliminar todos los caracteres de puntuación de la cadena
# En conjunto, maketrans('', '', string.punctuation) crea una tabla de traducción que no realiza ninguna sustitución de caracteres, pero especifica que se deben eliminar todos los caracteres de puntuación
# Luego, line.translate() se aplica a la variable line utilizando esta tabla de traducción. La función translate() toma la tabla de traducción y la aplica a la cadena, reemplazando los caracteres según las especificaciones de la tabla. En este caso, como solo se especificaron caracteres para eliminar, translate() eliminará todos los caracteres de puntuación de la cadena line, generando una nueva cadena donde se han eliminado los caracteres de puntuación.
# Espero que esta explicación sea más clara. Si tienes alguna otra pregunta, no dudes en preguntar.

# Si los argumentos cadena_de_entrada y cadena_de_salida en la función maketrans() se establecen en caracteres específicos en lugar de una cadena vacía, se realizará una traducción de caracteres.
# Cuando se establece cadena_de_entrada en un conjunto de caracteres y cadena_de_salida en otro conjunto de caracteres de la misma longitud, la función translate() reemplazará cada carácter en cadena_de_entrada con el carácter correspondiente en cadena_de_salida.
# Aquí hay un ejemplo para ilustrar esto:

import string
#lo que hace es que debe haber una entrada y salida con los mismos caracteres 
#los cuales seran reemplazados segun su equivalente por jerarquia de derecha a izquierda si la letra o caracter se repite
entrada = "hola mundo"
salida = "ya no hay0"

tabla = str.maketrans(entrada, salida, "")

texto = "abcdef"
texto_traducido = texto.translate(tabla)

print(texto_traducido)
# nbcyef   SALE ESO POR QUE (N) REFERENCIA (A) Y LA (D) REDERENCIA A (Y)

# 9.5 Depuración
# 
# Conforme trabajes con conjuntos de datos más grandes puede ser complicado depu-
# rar imprimiendo y revisando los datos a mano. Aquí hay algunas sugerencias para
# 
# depurar grandes conjuntos de datos:
# Reducir la entrada Si es posible, trata de reducir el tamaño del conjunto de
# 
# datos. Por ejemplo, si el programa lee un archivo de texto, comienza sola-
# mente con las primeras 10 líneas, o con el ejemplo más pequeño que puedas
# 
# encontrar. Puedes ya sea editar los archivos directamente, o (mejor) modi-
# ficar el programa para que solamente lea las primeras n número de líneas.
# 
# Si hay un error, puedes reducir n al valor más pequeño que produce el er-
# ror, y después incrementarlo gradualmente conforme vayas encontrando y
# 
# corrigiendo errores.
# Revisar extractos y tipos En lugar de imprimir y revisar el conjunto de datos
# completo, considera imprimir extractos de los datos: por ejemplo, el número
# de elementos en un diccionario o el total de una lista de números.
# Una causa común de errores en tiempo de ejecución es un valor que no es el
# tipo correcto. Para depurar este tipo de error, generalmente es suficiente con
# imprimir el tipo de un valor.
# Escribe auto-verificaciones Algunas veces puedes escribir código para revisar
# errores automáticamente. Por ejemplo, si estás calculando el promedio de
# una lista de números, podrías verificar que el resultado no sea más grande
# que el elemento más grande de la lista o que sea menor que el elemento más
# pequeño de la lista. Esto es llamado “prueba de sanidad” porque detecta
# resultados que son “completamente ilógicos”.
# Otro tipo de prueba compara los resultados de dos diferentes cálculos para
# ver si son consistentes. Esto es conocido como “prueba de consistencia”.
# Imprimir una salida ordenada Dar un formato a los mensajes de depuración
# puede facilitar encontrar un error.
# De nuevo, el tiempo que inviertas haciendo una buena estructura puede reducir el
# tiempo que inviertas en depurar.