# Clase 81 - Curso de Python - Sobre escritura de métodos pt2

## Notas de clase

### Introducción
Habrá ocasiones donde aunque nosotros ya hayamos sobre escrito los métodos de la clase padre tengamos la necesidad obligatoriamente de ejecutarlos, para estos casos lo mejor que podemos hacer es simplemente usar la función "super()".

### Sobre escritura de métodos pt2

La función "super()" nos permite acceder a la clase padre inmediata la cual facilmente podemos utilizar para ejecutar sus métodos, veamos un ejemplo.

```
class Animal(): # Clase Padre
    def comer(self):
        print('El animal come')

    def dormir(self):
        print('El animal duerme')


class Mascota(Animal): # Clase Padre convertida en hija
    
    def comer(self):
        print('La mascota come')

class Felino:

    def cazar(self):
        print('El felino caza')

class Gato(Mascota, Felino): # Clase hija
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer(self):
        super().comer()
        print(f'{self.nombre} come')

    def dormir(self):
        print(f'{self.nombre} duerme')


patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()
```

Como podemos observar en el ejemplo dentro de la clase "Gato" en el método de "comer" llamamos a la función "super()" seguido del método de la clase padre inmediata, que en este caso sería la clase "Mascota".



### Conclusión 

De esta manera tan simple podremos acceder a métodos de la clase padre aunque hayamos sobre escrito el método en una clase hija, se hará uso de la función "super()".