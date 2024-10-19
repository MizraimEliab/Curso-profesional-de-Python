# Clase 72 - Curso de Python - Clases

## Notas de clase

### Introducción
En Python podemos crear nuestras propias clases usando la palabra reservada "class".

### Clases

A continuación un ejemplo de una clase que represente a un usuario.

```
class Usuario:
```

Después de la palabra reservada de "class" va el nombre de la clase y esto se recomienda escribirlo con la nomenclatura "CamelCase" siempre y cuando el nombre de la clase de comprenda de 2 o más palabras.

Por convención el nombre de la clase deberá ser escrito en singular.

Dentro del bloque de código de la clase vamos a colocar todos los atributos y método que deseemos que la clase contenga.

En Python no podemos dejar bloques de código vacíos como el ejemplo de la clase, ya que el interprete nos marcará un error, para evitar esto bloque vacío podemos usar la palabra reservada "pass".

```
class Usuario:
    pass
```
Con "pass" le indicamos a Python que de momento ese bloque de código no hará ninguna acción y al ejecutarlo no nos dará error.

Ya con eso podremos crear una instancia de la clase como lo es propiamente un usuario.

```
class Usuario:
    pass

eliab = Usuario()
print(eliab)
```


### Conclusión 

De esta manera tan simple seremos capaces de tener clases en Python y a su vez objetos de estas clases. 