# Clases como tipos
# Como hemos visto, en Python todas las variables tienen un tipo. Podemos usar la
# función dir incluida en Python para examinar las características de una variable.
# También podemos usar type y dir con las clases que creemos.
class GrupoAnimal:
    x = 0
    
    def grupo(self) :
        self.x = self.x + 1
        print("Hasta ahora",self.x)

an = GrupoAnimal()
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.grupo))
