class Mascota: # Clase Padre
    def comer(self):
        print('La mascota come')

    def dormir(self):
        print('La mascota duerme')

class Perro(Mascota): # Clase Hija
    pass

class Gato(Mascota): # Clase hija
    pass

duke = Perro()

duke.comer()
duke.dormir()

patricio = Gato()

patricio.comer()
patricio.dormir()

# Herencia múltiple

class Animal(): # Clase Padre
    def comer(self):
        print('El animal come')

    def dormir(self):
        print('El animal duerme')


class Mascota(Animal): # Clase Padre convertida en hija
    pass

class Felino:

    def cazar(self):
        print('El felino caza')

class Gato(Mascota, Felino): # Clase hija
    pass

patricio = Gato()

patricio.comer()
patricio.dormir()
patricio.cazar()
