Una vez que recuperar documentos a través de HTTP y analizarlos usando pro-
gramas se convirtió en algo sencillo, no se tardó mucho en desarrollar un modelo

consistente en la producción de documentos específicamente diseñados para ser con-
sumidos por otros programas (es decir, no únicamente HTML para ser mostrado

en un navegador).
Existen dos formatos habituales que se usan para el intercambio de datos a través
de la web. El “eXtensible Markup Language” (lenguaje extensible de marcas), o

XML, ha sido utilizado durante mucho tiempo, y es el más adecuado para inter-
cambiar datos del tipo documento. Cuando los programas simplemente quieren

intercambiar diccionarios, listas u otra información interna, usan “JavaScript Ob-
ject Notation”, o JSON (Notación de Objetos Javascript; consulta www.json.org).

Nosotros examinaremos ambos formatos.

# 13.1 eXtensible Markup Language - XML
XML tiene un aspecto similar a HTML, pero más estructurado. Este es un ejemplo
de un documento XML:
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>
Cada par de etiquetas de apertura (p. ej., ‘’) y de cierre (p. ej., ‘’) representan
un elemento o nodo con el mismo nombre de la etiqueta (p. ej., ‘person’). Cada
elemento puede contener texto, atributos (p. ej., ‘hide’) y otros elementos anidados.
Si un elemento XML está vacío (es decir, no tiene contenido), puede representarse
con una etiqueta auto-cerrada (p. ej., ‘’).
A menudo resulta útil pensar en un documento XML como en la estructura de un
árbol, donde hay una etiqueta superior (en este caso ‘person’), y otras etiquetas
como ‘phone’ que se muestran como hijas de sus nodos padres.



# 13.4 JavaScript Object Notation - JSON
El formato JSON se inspiró en el formato de objetos y arrays que se usa en el
lenguaje JavaScript. Pero como Python se inventó antes que JavaScript, la sintaxis
usada en Python para los diccionarios y listas influyeron la sintaxis de JSON.
De modo que el formato del JSON es casi idéntico a la combinación de listas y
diccionarios de Python.

13.5. ANÁLISIS DE JSON 171
He aquí una codificación JSON que es más o menos equivalente al XML del ejemplo
anterior:
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}

Si te fijas, encontrarás ciertas diferencias. Primero, en XML se pueden añadir atrib-
utos como “intl” a la etiqueta “phone”. En JSON, simplemente tenemos parejas
clave-valor. Además, la etiqueta “person” de XML ha desaparecido, reemplazada
por un conjunto de llaves exteriores.
En general, las estructuras JSON son más simples que las de XML, debido a
que JSON tiene menos capacidades. Pero JSON tiene la ventaja de que mapea
directamente hacia una combinación de diccionarios y listas. Y, dado que casi
todos los lenguajes de programación tienen algo equivalente a los diccionarios y
listas de Python, JSON es un formato muy intuitivo para que dos programas que
vayan a cooperar intercambien datos.

JSON se está convirtiendo rápidamente en el formato elegido para casi todos los in-
tercambios de datos entre aplicaciones, debido a su relativa simplicidad comparado con XML.