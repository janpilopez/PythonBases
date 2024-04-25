Tres tipos de claves
Ahora que hemos empezado a construir un modelo de datos, colocando nuestros
datos en múltiples tablas enlazadas, y hemos enlazado las filas de esas tablas usando
claves, debemos fijarnos en cierta terminología acerca de esas claves. Generalmente,
en un modelo de base de datos hay tres tipos de claves que se pueden usar.
• Una clave lógica es una clave que se podría usar en el “mundo real” para
localizar una fila. En nuestro ejemplo de modelado de datos, el campo nombre
es una clave lógica. Es el nombre que se muestra en pantalla para el usuario y,
en efecto, usamos el campo nombre varias veces en el programa para localizar
la fila correspondiente a un usuario. Comprobarás que a menudo tiene sentido
añadir una restricción UNIQUE (única) a una clave lógica. Como las claves
lógicas son las que usamos para buscar una fila desde el mundo exterior,
tendría poco sentido permitir que hubiera múltiples filas con el mismo valor
en la tabla.

• Una clave primaria es normalmente un número que es asignado automáti-
camente por la base de datos. En general no tiene ningún significado fuera

del programa y sólo se utiliza para enlazar entre sí filas de tablas diferentes.
Cuando queremos buscar una fila en una tabla, realizar la búsqueda usando
la clave primaria es, normalmente, el modo más rápido de localizarla. Como

las claves primarias son números enteros, necesitan muy poco espacio de al-
macenamiento y pueden ser comparadas y ordenadas muy rápido. En nuestro

modelo de datos, el campo id es un ejemplo de una clave primaria.
• Una clave foránea (foreign key) es normalmente un número que apunta a la
clave primaria de una fila asociada en una tabla diferente. Un ejemplo de
una clave foránea en nuestro modelo de datos es la columna desde_id.
Estamos usando como convención para los nombres el darle siempre al campo de
clave primaria el nombre id y añadir el sufijo _id a cualquier nombre de campo
que sea una clave foránea.