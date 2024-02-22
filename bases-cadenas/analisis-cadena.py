#MOSTRAR SOLO EL DOMIDIO DEL CORREO
dato = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
arrobapos = dato.find('@')
print(arrobapos)
#especificamos buscar desde el indice arrobapos
espos = dato.find(' ',arrobapos)
print(espos)
#mostramos la cadena desde los indices encontrados
direccion = dato[arrobapos+1:espos]
print(direccion)

palabra = 'X-DSPAM-Confidence:0.8475'
espos = palabra.find(':')
print('El valor es %f' % float(palabra[espos+1:]) )