# Herencia
# Otra poderosa característica de la programación orientada a objetos es la capacidad
# de crear una nueva clase extendiendo una clase ya existente. Al extender una clase,
# llamamos a la clase original la clase padre y a la nueva clase clase hija.
# Por ejemplo, podemos mover a nuestra clase GrupoAnimal a su propio archivo.
# Luego, podemos ‘importar’ la clase GrupoAnimal en un nuevo archivo y extenderla,
# de la siguiente manera:
from multiples_instancias import GrupoAnimal 


class GrilloFan(GrupoAnimal):
    puntos = 0
    def seis(self):
        self.puntos = self.puntos + 6
        self.grupo()
        print(self.nombre,"puntos",self.puntos)

s = GrupoAnimal("Sally")
s.grupo()
j = GrilloFan("Jim") #Instanciamos el grupo animal dentro de grillo fan, entonces cuando pasamos jim se llama a la clase grupoanimal y se instancia jim
j.grupo()
j.seis()
print(dir(j))