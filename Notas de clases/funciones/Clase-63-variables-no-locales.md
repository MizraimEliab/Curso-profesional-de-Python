# Clase 63 - Curso de Python - Variables no locales

## Notas de clase

### Introducción
Se revisará el tema de clouses que esta relacionado con las funciones anidadas además de el alcance de las variables en las funciones.

Primeramente veremos como se comportan las variables dentro y fuera de las funciones, es decir, su alcance.

### Variables no locales

Vamos a ver este alcance de las variables con un ejemplo de una función principal y otra función anidada junto con sus variables.

```
def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'
        print(a)
        print(b)

    funcion_anidada()
    print(c)

funcion_principal()
```

Al analizar el código anterior podemos ver como la función principal cuenta con 2 variables y la función anidada tiene solamente una variable, pero, dentro de la función anidada hacemos uso de las variables de la función principal y viceversa, dentro de la función principal hacemos uso de la variable que se encuentra en la función anidada.

Este código obtendrá como salida la impresión de la variable a y b pero nos mostrará un error por la impresión de la variable c.

Esta salida es correcta debido a que la variable c se encuentra dentro del bloque de la función anidada por lo que la variable c es una variable local por esa razón no puede ser empleada fuera de la función anidada.

Las variables a y b de igual manera son variables locales ya que han sido creadas dentro del bloque de código de la función principal, pero, estas variables tienen un mayor alcance ya que se encuentran creadas en un bloque superior y puede ser empleadas en bloques inferiores, que en este caso es dentro de la función anidada.

Incluso si creamos una variable global como "e" por ejemplo, puede ser usada dentro de cualquier parte del programa, ya sea dentro o fuera de las funciones.

```
e = 'e' # Variable global

def funcion_principal():
    a = 'a' # Variable local
    b = 'b' # Variable local

    def funcion_anidada():
        c = 'c' # Variable local
        print(a)
        print(b)
        print(e)

    funcion_anidada()
    print(c)

funcion_principal()
```

Si quisiéramos modificar el valor de una variable de la función principal dentro de la función anidada pudiéramos reasignar el valor de la variable dentro de la función anidada, pero, esto no sería así ya que Python consideraría a b como 2 variable distintas ya que tienen scopes o alcances diferentes.

```
e = 'e' # Variable global

def funcion_principal():
    a = 'a' # Variable local
    b = 'b' # Variable local

    def funcion_anidada():
        c = 'c' # Variable local
        b = 'Cambio de valor'
        print(a)
        print(b)
        print(e)

    funcion_anidada()
    print(c)

funcion_principal()
```

Esto se puede comprobar imprimiendo el id de cada variable con la función "id" de Python.

Si quisiéramos cambiar el valor de una variable con un alcance superior como es la variable b deberemos usar  la palabra reservada "nonlocal" seguido de la variable del nivel superior que queramos modificar.

```
e = 'e' # Variable global

def funcion_principal():
    a = 'a' # Variable local
    b = 'b' # Variable local

    def funcion_anidada():
        c = 'c' # Variable local
        nonlocal b
        b = 'Cambio de valor'
        print(a)
        print(b)
        print(e)

    funcion_anidada()
    print(c)

funcion_principal()
```

Ahora estaremos cambiando el valor de la variable b que se encuentra en un nivel superior.


### Conclusión 

Las variables tienen diferentes alcances y cuando tenemos variables locales de un nivel superior en nuestras funciones que necesitemos cambiar en un nivel inferior deberemos usar "nonlocal" para indicarle a Python que estamos hablando de un mismo objeto.