
# OJO NO PONER EL MISMO NOMBRE DEL ARGUMENTO HABRA ERROR DE SINTAXIS, EL CODIGO FUNCIONARA PERO NO COMO QUEREMOS
# ESTE CODIGO IMPRIME EL NUMERO DE VECES QUE SE REPITE LA PALABRA
def Cuenta(palabra, letra_arg):
    contador = 0
    for letra in palabra:
        if letra == letra_arg:
            contador = contador + 1
            print(contador)

palabra = input('HOLA, INGRESA una palabra: \n');
letra = input('AHHORA, INGRESA una letra: \n');

Cuenta(palabra, letra)

while True:
    linea = input('INgresa algo >: ')
    # if linea[0] == '#' : Esto da error si no hay caracteres, podemos optimizarle como abajo
    if linea.startswith('#'): 
        continue #lo obvia y salta al siguiente ciclo while(reinicia)
    if linea == 'fin':
        break
    print(linea)
    
print('¡Terminado!')