# Clase 80 - Curso de Python - Sobre escritura de métodos

## Notas de clase

### Introducción
La sobre escritura de métodos o también conocida como la sobre carga de métodos es uno de los temas principales cuando se trabaja con programación orientada a objetos y consiste en que una clase hija puede modificar el comportamiento de los métodos de la clase padre, esto con la finalidad de que estos comportamientos se adecuen a las necesidades de la clase hija.

### Sobre escritura de métodos

Python primeramente cuando se hace una instancia de un objeto y se llamada a un método revisa si el método que se llama se encuentra dentro de la clase de la instancia, si no lo encuentra, buscará en un nivel superior, es decir, en la clase padre leyendo de izquierda a derecha.

Si en algún nivel queremos sobre escribir el método lo podemos hacer simplemente volviendo a escribir el método en el nivel que queramos sobre escribir.

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


patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()
```

Como se observa en el ejemplo anterior se sobre escribe el método "comer" dentro de la clase "Mascota". Para sobre escribir métodos basta con volver a definir el método con un comportamiento diferente.

Esto lo podemos hacer en el nivel menos abstracto de la herencia.

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
        print(f'{self.nombre} come')

    def dormir(self):
        print(f'{self.nombre} duerme')


patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()
```



### Conclusión 

Si ninguna de las clases posee el método Python solamente lanzará un error de que no ha encontrado la clase que el objeto esta mandando a llamar.

Antes de mostrar el error siempre buscará en nivel jerárquico. 