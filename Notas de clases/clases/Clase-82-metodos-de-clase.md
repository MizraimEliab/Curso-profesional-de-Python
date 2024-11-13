# Clase 82 - Curso de Python - Métodos de clase

## Notas de clase

### Introducción
Al igual que los atributos los métodos los podemos clasificar en 2 tipos, los métodos de instancia que le pertenecen a los objetos y los métodos de clase los cuales le pertenecen a la clase.

### Métodos de clase

Se harán uso de decoradores para trabajar con los métodos de clase.

```
class Circulo:

    pi = 3.141592

    @classmethod
    def area(cls, radio):
        return cls.pi * (radio ** 2)
    

resultado = Circulo.area(14)
print(resultado)
```

Como se observa en el ejemplo anterior para definir a un método de clase por convención para hacer el argumento que se refiera a la clase llevará el nombre de "cls" que usará el atributo de la clase para calcular el área de un circulo con un método de clase que esta usando el decorador "@classmethod" para indicarle a Python que el método es de clase y no de instancia.

Esto lo confirmamos ya que en la variable de "resultado" almacenamos lo que retorna el método directo de la clase sin la necesidad de crear un objeto.


### Conclusión 

De esta manera tan sencilla podemos definir y usar un método de clase, haciendo uso del decorador "@classmethod".