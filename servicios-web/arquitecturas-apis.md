Interfaces de programación de aplicaciones

Ahora tenemos la capacidad de intercambiar datos entre aplicaciones usando el Pro-
tocolo de Transporte de Hipertexto (HTTP), y un modo de representar estructuras

13.6. INTERFACES DE PROGRAMACIÓN DE APLICACIONES 173
de datos complejas para poder enviar y recibir los datos entre esas aplicaciones, a
través del eXtensibleMarkup Language (XML) o del JavaScript Object Notation
(JSON).
El paso siguiente es empezar a definir y documentar “contratos” entre aplicaciones
usando estas técnicas. El nombre habitual para estos contratos entre aplicaciones
es Interfaces de Programación de Aplicaciones (Application Program Interfaces), o
APIs. Cuando se utiliza una API, normalmente un programa crea un conjunto de

servicios disponibles para que los usen otras aplicaciones y publica las APIs (es de-
cir, las “reglas”) que deben ser seguidas para acceder a los servicios proporcionados

por el programa.
Cuando comenzamos a construir programas con funcionalidades que incluyen el
acceso a servicios proporcionados por otros programas, el enfoque se denomina
Service-Oriented Architecture (Arquitectura Orientada a Servicios), o SOA. Un
enfoque SOA es aquel en el cual nuestra aplicación principal usa los servicios de
otras aplicaciones. Un planteamiento no-SOA es aquel en el cual tenemos una

única aplicación independiente que contiene todo el código necesario para su im-
plementación.

Podemos encontrar multitud de ejemplos de SOAs cuando utilizamos servicios
de la web. Podemos ir a un único sitio web y reservar viajes en avión, hoteles
y automóviles, todo ello desde el mismo sitio. Los datos de los hoteles no están
almacenados en los equipos de la compañía aérea. En vez de eso, los computadores
de la aerolínea contactan con los servicios de los computadores de los hoteles,
recuperan los datos de éstos, y se los presentan al usuario. Cuando el usuario
acepta realizar una reserva de un hotel usando el sitio web de una aerolínea, ésta
utiliza otro servicio web en los sistemas de los hoteles para realizar la reserva
real. Y cuando llega el momento de cargar en tu tarjeta de crédito el importe de
la transacción completa, hay todavía otros equipos diferentes involucrados en el
proceso.

Una Arquitectura Orientada a Servicios tiene muchas ventajas, que incluyen: (1)
siempre se mantiene una única copia de los datos (lo cual resulta particularmente

importante en ciertas áreas como las reservas hoteleras, donde no queremos du-
plicar excesivamente la información) y (2) los propietarios de los datos pueden

imponer reglas acerca del uso de esos datos. Con estas ventajas, un sistema SOA
debe ser diseñado cuidadosamente para tener buen rendimiento y satisfacer las
necesidades de los usuarios.
Cuando una aplicación ofrece un conjunto de servicios en su API disponibles a
través de la web, los llamamos servicios web.