# Desplazamiento a través de los nodos
# A menudo el XML tiene múltiples nodos y tenemos que escribir un bucle para
# procesarlos todos. En el programa siguiente, usamos un bucle para recorrer todos
# los nodos ‘usuario’:
import xml.etree.ElementTree as ET
datos = '''
    <cosa>
        <usuarios>
            <usuario x="2">
                <id>001</id>
                <nombre>Chuck</nombre>
            </usuario>
            <usuario x="7">
                <id>009</id>
                <nombre>Brent</nombre>
            </usuario>
        </usuarios>
    </cosa>'''
cosa = ET.fromstring(datos)
lst_usuarios = cosa.findall('usuarios/usuario')
print('Total de usuarios:', len(lst_usuarios))
for item in lst_usuarios:
    print('--------------')
    print('Nombre', item.find('nombre').text)
    print('Id', item.find('id').text)
    print('Atributo', item.get('x'))
# Código: https://es.py4e.com/code3/xml2.py

# El método ‘findall’ devuelve una lista de subárboles que representan las estructuras
# ‘usuario’ del árbol XML. A continuación podemos escribir un bucle ‘for’ que busque
# en cada uno de los nodos usuario, e imprima el texto de los elementos ‘nombre’ e
# ‘id’, además del atributo ‘x’ de cada nodo usuario.



# Es importante incluir todos los elementos base en la declaración de ‘findall’  (p. ej., ‘usuarios/usuario’). Excep-
# tuando aquel que se encuentra en el nivel superior por ejemplo (p. ej., ‘cosa/usuarios/usuario’). De
# lo contrario, Python no encontrará ninguno de los nodos que buscamos.
import xml.etree.ElementTree as ET
input = '''
<cosa>
    <usuarios>
        <usuario x="2">
            <id>001</id>
            <nombre>Chuck</nombre>
        </usuario>
        <usuario x="7">
            <id>009</id>
            <nombre>Brent</nombre>
        </usuario>
    </usuarios>
</cosa>'''
cosa = ET.fromstring(input)
lst = cosa.findall('usuarios/usuario')
print('Cuenta de usuarios:', len(lst))
lst2 = cosa.findall('usuario')
print('Cuenta de usuarios:', len(lst2))
lst3 = cosa.findall('cosas/usuarios/usuario')
print('Cuenta de usuarios:', len(lst3))
# ‘lst’ almacena todos los elementos ‘usuario’ anidados dentro de su base ‘usuarios’.

# ‘lst2’ busca los elementos ‘usuario’ que no se encuentren anidados dentro del ele-
# mento de nivel superior ‘cosa’ donde no hay ninguno.

# Cuenta de usuarios: 2
# Cuenta de usuarios: 0
# Cuenta de usuarios: 0
