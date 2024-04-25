import sqlite3
conn = sqlite3.connect('musica.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Canciones')
cur.execute('CREATE TABLE Canciones (titulo TEXT, reproducciones INTEGER)')
conn.close()

La operación connect realiza una conexión con la base de datos almacenada en el
archivo musica.sqlite en el directorio actual. Si el archivo no existe, se creará
uno nuevo. La razón de que se le llame una “conexión” es que a veces la base
de datos se almacena en un “servidor de bases de datos”, distinto del servidor en
el cual está funcionando nuestra aplicación. En nuestros ejemplos, dado que son
sencillos, la base de datos será simplemente un archivo local en el mismo directorio
en el que está funcionando el código de Python.

Un cursor es como un manejador de archivos, y se puede usar para realizar op-
eraciones en los datos almacenados en la base de datos. La llamada a cursor()

es muy similar conceptualmente a la llamada open() cuando se está tratando con
archivos de texto.
Una vez que tenemos el cursor, podemos comenzar a ejecutar comandos sobre el
contenido de la base de datos, usando el método execute().
El primer comando SQL elimina la tabla Canciones si ya existe. Este

planteamiento se utiliza simplemente para permitirnos ejecutar el mismo pro-
grama para crear la tabla Canciones una y otra vez sin provocar un error.

Observa que el comando DROP TABLE elimina la tabla y todo su contenido de la
base de datos (es decir, aquí no existe la opción “deshacer”).
cur.execute('DROP TABLE IF EXISTS Canciones ')
El segundo comando crea una tabla llamada Canciones con una columna de texto
llamada titulo y una columna de enteros llamada reproducciones.
cur.execute('CREATE TABLE Canciones (titulo TEXT, reproducciones INTEGER)')
Ahora que ya hemos creado la tabla llamada Canciones, podemos guardar algunos
datos en ella usando la operación de SQL INSERT. Empezaremos realizando otra
vez una conexión con la base de datos y obteniendo el cursor. Luego podemos
ejecutar comandos SQL usando ese cursor.

El comando INSERT de SQL indica qué tabla se está utilizando y luego de-
fine una fila nueva, enumerando los campos que se desean incluir (titulo,

reproducciones) seguidos por los valores (VALUES) que queremos colocar en esa
fila. Nosotros vamos a especificar los valores como signos de interrogación (?, ?)
para indicarle que los valores reales serán pasados como una tupla ( 'My Way',
15 ) en el segundo parámetro de la llamada a execute().