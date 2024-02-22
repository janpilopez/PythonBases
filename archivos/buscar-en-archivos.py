#HAY QUE LEERLO UTILIZANDO UN CICLO FOR O WHILE
manejador_archivo = open('C:/Users/jp/Documents/Python/archivos/mbox.txt')
for linea in manejador_archivo:
    linea = linea.rstrip()#ELIMINA LOS ESPACIOS EN BLANCO DEL LADO DERECHO DE LA CADENA
    if linea.startswith('From:'):
        print(linea)
#REALIZA LO MISMO PERO PODEMOS REALIZAR MAS ACCIONES
# Podemos estructurar el bucle para seguir el patrón de ignorar las líneas no interesantes así:
man_a = open('C:/Users/jp/Documents/Python/archivos/mbox.txt')
for linea in man_a:
    linea = linea.rstrip()
    # Ignorar 'líneas que no nos interesan'
    if not linea.startswith('From:'):
        continue
    # Procesar la línea que nos 'interesa'
    print(linea)

#BUSCAMOS CADENA COINCIDEN, SI NO ENCUENTRA RETORNA -1, SI ENCUENTRA ES LA POSICION DE LA LINEA
man_a = open('C:/Users/jp/Documents/Python/archivos/mbox.txt')
for linea in man_a:
    linea = linea.rstrip()
    if linea.find('@uct.ac.za') == -1: continue
    print(linea)


narchivo = input('Ingresa un nombre de archivo: ')
if(narchivo == 'na na boo boo'):
        print('TE HE ATRAPADO NANA BOBO')
        exit()
        
else:
    try:
            man_a = open(narchivo)
    except:
        print('No se puede abrir el archivo:', narchivo)
        exit()
            
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay', contador, 'líneas de asunto (subject) en', narchivo)
# Código: https://es.py4e.com/code3/search7.py
# La función exit termina el programa. Es una función que llamamos que nunca
# retorna. Ahora cuando nuestro usuario (o el equipo de QA) introduzca algo sin
# sentido o un nombre de archivo incorrecto, vamos a “capturarlo” y recuperarnos
# de forma elegante: