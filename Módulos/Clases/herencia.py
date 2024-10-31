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