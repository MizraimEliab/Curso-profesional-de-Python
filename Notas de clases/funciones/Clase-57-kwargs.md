# Clase 57 - Curso de Python - Kwargs

## Notas de clase

### Introducción

Es posible en Python trabajar con más de un asterisco en un parámetro, sin embargo, esto implicaría que dejemos de trabajar con tuplas y comencemos a trabajar con diccionarios.

### Kwargs

Por convención de la comunidad Python este argumento debe ser nombrado después del uso de doble asterisco como "kwargs"

Este parámetro automáticamente se convierte en un diccionario.

Veamos un ejemplo de una función cuyos valores sean calificaciones de usuarios.

```
def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(alan=[10, 10, 8], fernando=[10, 9, 9])
```

En este ejemplo podemos observar que los parámetros son utilizados como llaves del diccionario y sus valores como los valores usados para los parámetros al momento de llamar la función.

Es importante mencionar que podemos tener ambos parámetros e una sola función y usar "args" y "kwargs" en una sola función.

```
def coninacion(*args, **kwargs):
    print(args)
    print(kwargs)

conbinacion(1, 2, 3, 4, 5, algo=True, palabra='Python')
```

### Conclusión 

"kwargs" nos ayuda a manejar de una manera distinta nuestros datos de entrada en las funciones que ocupemos ya que nos guarda la información a manera de diccionario apoyando al uso de la información.