manejador = open('C:/Users/jp/Documents/Python/archivos/mbox-short.txt')
for linea in manejador:
    palabras = linea.split()
    if len(palabras) == 0 or len(palabras) <= 1: continue #agregamos esto porque puede que una linea completa este vacio osea sea un salto e linea
                                        #y tambien verificamos que len tenga al menos 3 valores(2) osea el dia de semana porque solo puede tener from y nada mas
                                            # From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    if palabras[0] != 'From' : continue
    print(palabras[2])#dia de semana