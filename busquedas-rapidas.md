Depuración
Python incluye una documentación simple y rudimentaria que puede ser de gran
ayuda si necesitas revisar para encontrar el nombre exacto de algún método. Esta
documentación puede revisarse en el intérprete de Python en modo interactivo.
Para mostrar el sistema de ayuda interactivo, se utiliza el comando help().
>>> help()
help> modules
Si sabes qué método quieres usar, puedes utilizar el comando dir() para encontrar
los métodos que contiene el módulo, de la siguiente manera:
>>> import re
>>> dir(re)
[.. 'compile', 'copy_reg', 'error', 'escape', 'findall',
'finditer' , 'match', 'purge', 'search', 'split', 'sre_compile',
'sre_parse' , 'sub', 'subn', 'sys', 'template']
También puedes obtener una pequeña porción de la documentación de un método
en particular usando el comando dir.
>>> help (re.search)
Help on function search in module re:
search(pattern, string, flags=0)
Scan through string looking for a match to the pattern, returning
a match object, or None if no match was found.
>>>
La documentación incluida no es muy exhaustiva, pero puede ser útil si estás con
prisa o no tienes acceso a un navegador o motor de búsqueda.