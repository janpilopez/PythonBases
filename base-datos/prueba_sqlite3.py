import sqlite3
conn = sqlite3.connect('musica.sqlite')
cur = conn.cursor()
cur.execute('INSERT INTO Canciones (titulo, reproducciones) VALUES (?, ?)',
                ('Thunderstruck', 20)
            )
cur.execute('INSERT INTO Canciones (titulo, reproducciones) VALUES (?, ?)',
                ('My Way', 15)
            )
conn.commit()
print('Canciones:')
cur.execute('SELECT titulo, reproducciones FROM Canciones')
for fila in cur:
    print(fila)
cur.execute('DELETE FROM Canciones WHERE reproducciones < 100')
conn.commit()
cur.close()

# Primero insertamos (INSERT) dos filas en la tabla y usamos commit() para forzar
# a que los datos sean escritos en el archivo de la base de datos.
# Después usamos el comando SELECT para recuperar las filas que acabamos de in-
# sertar en la tabla. En el comando SELECT, indicamos qué columnas nos gustaría
# obtener (titulo, reproducciones), y también desde qué tabla queremos recu-
# perar los datos. Después de ejecutar la sentencia SELECT, el cursor se convierte
# en algo con lo que podemos iterar mediante una sentencia for. Por eficiencia, el
# cursor no lee todos los datos de la base de datos cuando se ejecuta la sentencia
# SELECT. En lugar de ello, los datos van siendo leídos a medida que se van pidiendo
# las filas desde el bucle creado con la sentencia for.