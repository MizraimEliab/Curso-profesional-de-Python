# Clase 70 - Curso de Python - Documentar funciones

## Notas de clase

### Introducción
Una muy buena práctica de programación al momento de crear funciones es que siempre que podamos las documentemos y para ello utilizando Python nos apoyaremos de "Docstring" . 

### Documentar funciones

Un "Docstring" es un comentario que se coloca en la primera línea de código de nuestra función. 

Trabajemos con una función para ver un ejemplo.


```
def suma(numero_uno, numero_dos):
    """
    La función suma dos números enteros.

    Argumentos:
    numero_uno (int)
    numero_dos (int)

    Se retorna la suma de los parámetros.
    """
    return numero_uno + numero_dos
```

Como podemos observar en el ejemplo anterior el "Docstring" es el comentario que se encuentra dentro de nuestra función donde describe el funcionamiento de la misma.

Dentro del comentario la primera línea es una breve descripción de lo que realiza la función y posteriormente podemos detallar cada parte de la función como los argumentos, los valores que se retornan e incluso esta permitido agregar un todo list.

El "Docstring" quedará almacenado en el atributo "__doc__" ya que en Python existen objetos documentables, este tipo de objetos poseen el atributo "__doc__" y mediante este atributo nosotros seremos capaces de comentar su respectiva documentación.

Los objetos documentables son los siguientes.

    - Módulos
    - Clases
    - Métodos
    - Funciones

En el ejemplo el "Docstring" será almacenado en el atributo "__doc__" de nuestra función y podemos confirmar esto imprimiendo en consola el atributo.

```
print(suma.__doc__)

```

Este código nos mostrará la documentación de la función, de igual manera podemos hacer uso de la función "help()" pasando como argumento el nombre de nuestra función y obtendremos el mismos resultado, es decir, la documentación de la función.

```
print(help(suma))
```


### Conclusión 

Siempre que creemos una función es muy recomendable documentarla y para ello se hace uso del "Docstring" que de manera simple es un comentario que se coloca en la primer línea de código de nuestra función y por convención se usa la triple comillas dobles.