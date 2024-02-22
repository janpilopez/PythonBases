palabra = str(input('HOLA, INGRESA una palabra: \n'))
palabra = palabra.lower()
if palabra == 'banana':
    print('Muy bien, bananas.')

#NO FUNCIONA CON LAS MAYUSCULAS SI NO ES IGUAL LA DETECTARA COMO MENOS
if palabra < 'banana': #compara los caracteres(length) si tiene menos
    print('Tu palabra, ' + palabra + ', está antes de banana.')
elif palabra > 'banana': #compara los caracteres si tiene mas
    print('Tu palabra, ' + palabra + ', está después de banana.')
else:#si es igual
    print('Muy bien, bananas.')