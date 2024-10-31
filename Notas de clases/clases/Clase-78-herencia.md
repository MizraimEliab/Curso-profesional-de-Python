# Clase 78 - Curso de Python - Herencia

## Notas de clase

### Introducción
En términos simples la herencia es cuando 2 clases tienen relación entre ellas.

### Herencia

Para ejemplificar el concepto vamos a apoyarnos de 2 clases una que se llame "Mascota" y otra llamada "Perro".

```
class Mascota: # Clase Padre
    def comer(self):
        print('La mascota come')

    def dormir(self):
        print('La mascota duerme')

class Perro(Mascota): # Clase Hija
    pass


duke = Perro()

duke.comer()
duke.dormir()
```

Para poder realizar la herencia dentro de la clase hija que es la clase "Perro" vamos a colocar entre paréntesis como se muestra el ejemplo el nombre de la clase padre que es "Mascota" y al hacer esto los objetos de tipo Perro podrán acceder a todos aquellos atributos y métodos que se encuentren dentro de la clase "Mascota".

En el ejemplo anterior se muestra la instancia del objeto "Perro" que es "duke" como puede acceder a los métodos de la clase padre "Mascota" aunque dichos métodos no se encuentren en la clase "Pedro" pero es posible acceder a ellos porque la clase "Perro" hereda de la clase "Mascota" que si tiene los métodos, por lo tanto, los atributos y métodos de la clase padre estarán disponibles en la clase hija.

Algo importante a mencionar es que una clase puede convertirse en clase padre una cantidad n de veces, es decir, podemos definir otra clase por ejemplo "Gato" que también herede de la clase "Mascota".


```
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
```


### Conclusión 

Después del nombre de la clase se colocan los paréntesis y se indica el nombre de la clase padre.