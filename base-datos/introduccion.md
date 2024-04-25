¿Qué es una base de datos?

Una base de datos es un archivo que está organizado para almacenar datos. La
mayoría de las bases de datos están organizadas como diccionarios, en el sentido de
que realizan asociaciones entre claves y valores. La diferencia más importante es
que la base de datos se encuentra en el disco (u otro almacenamiento permanente),
de modo que su contenido se conserva después de que el programa finaliza. Gracias
a que la base de datos se guarda en almacenamiento permanente, puede almacenar
muchos más datos que un diccionario, que está limitado al tamaño de memoria
que tenga la computadora.
Como un diccionario, el software de una base de datos está diseñado para conseguir
que la inserción y acceso a los datos sean muy rápidos, incluso para grandes canti-
dades de datos. Este software mantiene su rendimiento mediante la construcción
de índices, como datos añadidos a la base de datos que permiten al equipo saltar
rápidamente hasta una entrada concreta.
Existen muchos sistemas de bases de datos diferentes, que se utilizan para una
amplia variedad de propósitos. Algunos de ellos son: Oracle, MySQL, Microsoft
SQL Server, PostgreSQL, y SQLite. En este libro nos enfocaremos en SQLite,
ya que se trata de una base de datos muy común y ya viene integrada dentro de
Python. SQLite está diseñada para ser incrustada dentro de otras aplicaciones, de
modo que proporcione soporte para bases de datos dentro de la aplicación. Por
ejemplo, el navegador Firefox es uno de los que utilizan la base de datos SQLite
internamente, al igual que muchos otros productos.
http://sqlite.org/
SQLite es muy adecuado para ciertos problemas de manipulación de datos que
nos encontramos en informática, como en la aplicación de rastreo de Twitter que
hemos descrito en el capítulo anterior.