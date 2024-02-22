try:
   def Cuenta(palabra, letra_arg):
    contador = 0
    for letra in palabra:
        if letra == letra_arg:
            contador = contador + 1
            print(contador)

    palabra = str(input('HOLA, INGRESA una palabra: \n'))

    letra = str(input('AHHORA, INGRESA una letra: \n'))

    Cuenta(palabra, letra);

except:
    print('INGRESE UNA PALABRA CORRECTA')