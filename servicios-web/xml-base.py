# Análisis de XML
# He aquí una aplicación sencilla que analiza un archivo XML y extrae algunos
# elementos de él:
import xml.etree.ElementTree as ET
datos = '''
    <persona>
        <nombre>Chuck</nombre>
        <telefono type="intl">
        +1 734 303 4456
        </telefono>
        <email oculto="si" />
    </persona>
    '''
arbol = ET.fromstring(datos)
print('Nombre:', arbol.find('nombre').text)
print('Atributo:', arbol.find('email').get('oculto'))

# Tanto la triple comilla simple (‘”‘’) como la triple comilla doble (’“”“’) permiten
# la creación de cadenas que abarquen varias líneas.
# La llamada a ‘fromstring’ convierte la representación de cadena del XML en un
# “árbol” de nodos XML. Una vez tenemos el XML como un árbol, disponemos de
# una serie de métodos que podemos llamar para extraer porciones de datos de ese
# XML. La función ‘find’ busca a través del árbol XML y recupera el nodo que
# coincide con la etiqueta especificada.

# El usar un analizador de XML como ‘ElementTree’ tiene la ventaja de que, a pesar
# de que el XML de este ejemplo es bastante sencillo, resulta que hay muchas reglas
# relativas a la validez del XML, y el uso de ‘ElementTree’ nos permite extraer datos
# del XML sin preocuparnos por esas reglas de sintaxis.