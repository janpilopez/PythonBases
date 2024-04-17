# Podemos utilizar un programa similiar al tenrior procotolo-http-py para recibir
# una imagen utilizando HTTP. En vez de copiar los datos a la pantalla conforme
# va funcionando el programa, vamos a guardar los datos en una cadena, remover
# la cabecera, y después guardar los datos de la imagen en un archivo tal como se
# muestra a continuación:

import socket
import time
SERVIDOR = 'data.pr4e.org'
PUERTO = 80
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect((SERVIDOR, PUERTO))
misock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n') #enviar query #Si utilizamos b es byte (encode= entonces ya no es necesario)
contador = 0
imagen = b""
while True:
    datos = misock.recv(5120) #Especificamos que solicitamos 5120 caracteres
    if len(datos) < 1: break #Si no hay datos por recibir o ha sido cargado todo, salimos del bucle
    time.sleep(0.25) #Si habilitamos timeslip habra un retraso espera y podra cargar los 5120 caracteres, si no esta habilitado dependera de la velocidad de la red
    contador = contador + len(datos)
    print(len(datos), contador)
    imagen = imagen + datos
misock.close()
# Búsqueda del final de la cabecera (2 CRLF), siempre tiene dos saltos de linea
pos = imagen.find(b"\r\n\r\n")
print('\n **********Header length', pos)
print('\n //////////ENCABEZADO',imagen[:pos].decode())

# Ignorar la cabera y guardar los datos de la imagen
imagen = imagen[pos+4:] #recordemos que cada salto de linea es de 1 caracter, cada \r es un caracter y cada \n es un caracter como son 4 en total se ubica 4


fhand = open("cosa.jpg", "wb")
fhand.write(imagen)
fhand.close()
# Código: https://es.py4e.com/code3/urljpeg.py