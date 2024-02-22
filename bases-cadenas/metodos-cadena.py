
#FIND - buscar posicion de un elemento coincidente dentro de una cadena
palabra = 'banana'
indice = palabra.find('a')
print(indice)
#El método find puede encontrar subcadenas así como caracteres:
print(palabra.find('na'))
#También puede tomar como un segundo argumento el índice desde donde debe empezar:
palabra.find('na', 3)

#STRIP - ELIMINA LOS ESPACIO EN BLANCO blanco (espacios, tabs, o nuevas líneas) en el inicio y el final de una cadena
linea = ' Aquí vamos '
print(linea.strip())

#startswith devuelven valores booleanos si encuentra coincidencias
linea = 'Que tengas un buen día'
print(linea.startswith('Que'))
print(linea.startswith('q'))
print(linea.lower().startswith('q')) #Convertimos la cadena linea  minuscula y ahora si encontrara diferencias
