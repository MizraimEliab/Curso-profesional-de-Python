# Clase 79 - Curso de Python - Herencia múltiple

## Notas de clase

### Introducción
Algo interesante de Python en comparación con otros lenguajes de programación es que Python permite la herencia múltiple, esto quiere decir que una clase puede heredar de múltiples clases.

### Herencia múltiple

Para ver la herencia múltiple vamos a revisar un ejemplo.

```
class Mascota: # Clase Padre
    def comer(self):
        print('La mascota come')

    def dormir(self):
        print('La mascota duerme')

class Felino:

    def cazar(self):
        print('El felino caza')

class Gato(Mascota, Felino): # Clase hija
    pass
```

Como podemos observar la clase "Gato" esta heredando de 2 clases y esto se indica con la herencia, solamente que usamos una coma para separar las clases padres "Mascota" y "Felino".

Esto quiere decir que todos los objetos de tipo "Gato" pueden acceder a los atributos y métodos de la clase "Mascota" y la clase "Felino".

El ejemplo completo quedaría de la siguiente manera.


```
class Mascota: # Clase Padre
    def comer(self):
        print('La mascota come')

    def dormir(self):
        print('La mascota duerme')

class Felino:

    def cazar(self):
        print('El felino caza')

class Gato(Mascota, Felino): # Clase hija
    pass

patricio = Gato()

patricio.comer()
patricio.dormir()
patricio.cazar()
```

Esto tiene muchas ventajas, principalmente cuando nosotros queremos extender funcionalidades para nuestros objetos. Para finalizar cabe resaltar que las clases padres se pueden convertir en clases hijas ya que estas clases de igual manera pueden heredar de otras clases.

```
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
```


### Conclusión 

En Python podemos implementar la herencia múltiple es decir que una clase herede de varias clases y para ello solo basta con colocar dentro de los parentesis separadas mediante una coma todas aquellas clases de las cuales queramos heredar.