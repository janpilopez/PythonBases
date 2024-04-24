class GrupoAnimal:
    x = 0
    
    def __init__(self):
        print('Estoy construido')
    
    def grupo(self) :
        self.x = self.x + 1
        print('Hasta ahora',self.x)
    
    def __del__(self):
        print('Estoy destruido', self.x)
        
an = GrupoAnimal()
an.grupo()
an.grupo()
an = 42
print('an contiene',an)

# efectivamente “tira a la basura” el objeto para reutilizar la variable an, almace-
# nando el valor 42. Justo en el momento en que nuestro objeto an está siendo
# “destruido” se llama a nuestro código destructor (__del__). No podemos evitar
# que nuestra variable sea destruida, pero podemos efectuar la configuración que
# resulte necesaria antes de que el objeto deje de existir.
# Al desarrollar objetos, es bastante común agregarles un constructor que fije sus
# valores iniciales (init). Es relativamente raro necesitar un destructor para un objeto.