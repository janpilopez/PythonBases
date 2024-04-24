class GrupoAnimal:
    x = 0
    nombre = ''
    
    def __init__(self, nom):
        self.nombre = nom
        print(self.nombre,'construido')
    
    def grupo(self) :
        self.x = self.x + 1
        print(self.nombre,'recuento grupal',self.x)
        
# s = GrupoAnimal('Sally')
# j = GrupoAnimal('Jim')
# s.grupo()
# j.grupo()
# s.grupo()

# El constructor tiene tanto un parámetro self, que apunta a la instancia del objeto,
# como parámetros adicionales, que se pasan al constructor al momento de construir
# el objeto:
# s = GrupoAnimal('Sally')
# Dentro del constructor, la segunda línea copia el parámetro (nom), el que se pasa
# al atributo nombre dentro del objeto.
# self.nombre = nom
# El resultado del programa muestra que cada objeto (s y j) contienen sus propias
# copias independientes de x y nom: