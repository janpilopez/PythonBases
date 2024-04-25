# Rastreo en Twitter usando una base de datos
# En esta sección, crearemos un programa araña sencillo que se moverá a través de
# cuentas de Twitter y construirá una base de datos de ellas. Nota: Ten mucho
# cuidado cuando al ejecutar este programa. Si extraes demasiados datos o ejecutas
# el programa durante demasiado tiempo pueden terminar cortándote el acceso a
# Twitter.

from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('arana.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (nombre TEXT, recuperado INTEGER, amigos INTEGER)''')

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    cuenta = input('Ingresa una cuenta de Twitter, o salir: ')
    if (cuenta == 'salir'): break
    if (len(cuenta) < 1):
        cur.execute('''SELECT nombre FROM Twitter 
            WHERE recuperado = 0 LIMIT 1''')
        try:
            cuenta = cur.fetchone()[0]
        except:
            print('No se han encontrado cuentas de Twitter por recuperar')
            continue

    url = twurl.aumentar(TWITTER_URL, {'screen_name': cuenta, 'count': '5'})
    print('Recuperando', url)
    conexion = urlopen(url, context=ctx)
    datos = conexion.read().decode()
    cabeceras = dict(conexion.getheaders())

    print('Restante', cabeceras['x-rate-limit-remaining'])
    js = json.loads(datos)
    # DepuraciÃ³n
    # print json.dumps(js, indent=4)

    cur.execute('''UPDATE Twitter 
            SET recuperado=1 WHERE nombre = ?''', (cuenta, ))

    contnuevas = 0
    contantiguas = 0
    for u in js['users']:
        amigo = u['screen_name']
        print(amigo)
        cur.execute('SELECT amigos FROM Twitter WHERE nombre = ? LIMIT 1',
                    (amigo, ))
        try:
            contador = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET amigos = ? WHERE nombre = ?',
                        (contador+1, amigo))
            contantiguas = contantiguas + 1
        except:
            cur.execute('''INSERT INTO Twitter (nombre, recuperado, amigos)
                        VALUES (?, 0, 1)''', (amigo, ))
            contnuevas = contnuevas + 1
    print('Cuentas nuevas=', contnuevas, ' ya visitadas=', contantiguas)
    conn.commit()

cur.close()


# Restricciones en tablas de bases de datos
# Conforme diseñamos la estructura de la tabla, podemos indicar al sistema de la
# base de datos que queremos aplicar algunas reglas. Estas reglas nos ayudarán a
# evitar errores y a introducir correctamente los datos en las tablas. Cuando creamos
# nuestras tablas:
# cur.execute('''CREATE TABLE IF NOT EXISTS Personas
# (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE, recuperado INTEGER)''')
# cur.execute('''CREATE TABLE IF NOT EXISTS Seguimientos
# (desde_id INTEGER, hacia_id INTEGER, UNIQUE(desde_id, hacia_id))''')
# con unique especificamos que no pueden existir datos duplicados poor loque lo obviara evitando errores


# Después, podemos aprovechar estas restricciones en el código siguiente:
# cur.execute('''INSERT OR IGNORE INTO Personas (nombre, recuperado)
# VALUES ( ?, 0)''', ( amigo, ) )
# Aquí añadimos la clausula OR IGNORE en la sentencia INSERT para indicar que si
# este INSERT en particular causara una violación de la regla “el nombre debe ser
# único”, el sistema de la base de datos está autorizado a ignorar el INSERT. De
# esta forma, estamos usando las restricciones de la base de datos como una red de
# seguridad para asegurarnos de que no hacemos algo incorrecto sin darnos cuenta.