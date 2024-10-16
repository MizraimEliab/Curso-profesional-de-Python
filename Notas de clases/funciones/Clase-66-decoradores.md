# Clase 66 - Curso de Python - Decoradores

## Notas de clase

### Introducción
A través de los decoradores seremos capaces de reducir líneas de código duplicadas, haremos que el código se más legible, fácil de testear y fácil de mantener.

Un decorador es una función la cual toma como valor de entrada una función y a su vez retorna otra función.

Puede sonar confuso, sin embargo, cuando trabajamos con un decorador hay que tener en mente que estaremos haciendo uso de al menos 3 funciones (La entrada, la salida y la función principal).

### Decoradores

Vamos a hacer uso de decoradores siempre que queramos extender funcionalidades a una función ya sea porque no podemos modificar la función o simplemente no queremos hacerlo.

Vamos a revisar un ejemplo de la estructura base de un decorador.

```
# Decoradores
"""
a -> La función principal (Decorador)
b -> La función a decorar
c -> La función decorada

a(b) -> c
"""
# Estructura base de un decorador
def funcion_a(funcion_b):

    def funcion_c():
        pass
    
    return funcion_c
```

Ahora veremos un ejemplo aplicando esta estructura base de un decorador.

```
def funcion_a(funcion_b):

    def funcion_c():
        pass
    
    return funcion_c

@funcion_a
def saludar():
    print('Hola Mundo!')

saludar()
```

Lo que se puede observar en el ejemplo anterior es como usamos la función "saludar" como parámetro de la función a y esto se hace mediante un arroba y el nombre de la función principal que en este caso es la función a , esto se pone justo arriba de la función "saludar".

Si ejecutamos el ejemplo anterior no obtendremos ningún resultado, esto se debe que al mandar a una función decorada no estaremos ejecutando esa función, si no que, estaremos ejecutando la función que retorne el decorador (en este caso la función c debido a que la retorna la función a).

En este caso la función c no hace nada por ello al mandar a ejecutar la función de "saludar" no vemos nada en la consola.

Si modificamos la función c y colocamos un mensaje lo podríamos ver.

```
# Estructura base de un decorador
def funcion_a(funcion_b):

    def funcion_c():
        #pass
        print('Hola desde la función c')
    
    return funcion_c

@funcion_a
def saludar():
    print('Hola Mundo!')

saludar()
```

Si quisiéramos ejecutar la función a decorar (función b) que viene siendo la función "saludar" en el decorador deberemos dentro de la función c mandar a llamar el parámetro de función b.

```
# Estructura base de un decorador
def funcion_a(funcion_b):

    def funcion_c():
        #pass
        #print('Hola desde la función c')
        funcion_b
    
    return funcion_c

@funcion_a
def saludar():
    print('Hola Mundo!')

saludar()
```

Con esto podemos realizar diferentes tareas antes y después del llamado de la función a decorar y es aquí donde podemos extender las funcionalidades de nuestras funciones antes y después de su llamado.

```
# Estructura base de un decorador
def funcion_a(funcion_b):

    def funcion_c():
        #pass
        #print('Hola desde la función c')
        print('>>>>> Antes del llamado')
        funcion_b
        print('>>>>> Después del llamado')
    
    return funcion_c

@funcion_a
def saludar():
    print('Hola Mundo!')

saludar()
```


### Conclusión 

Los decoradores soy muy útiles cuando queremos extender las funcionalidades de una función en caso de que no podamos o no queramos modificar dicha función.

Un decorador puede ser usado una n cantidad de veces además de n cantidad de funciones.