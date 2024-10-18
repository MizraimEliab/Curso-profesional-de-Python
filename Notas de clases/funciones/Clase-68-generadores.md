# Clase 68 - Curso de Python - Generadores

## Notas de clase

### Introducción
Un generador es un tipo especial de función las cual retorna objetos que fácilmente podemos iterar, esto sin que la función finalice.

### Generadores

Vamos a trabajar con un ejemplo de un generadores que nos permita iterar todos los números pares que comprendan del 0 al 100.

```
def pares():
    for numero in range(0, 100, 2):
        return numero

print(pares())
```

Este código es una función que no es un generador debido a que hacemos uso de "return" y si recordamos la palabra reservada de "return" retorna un objeto y finaliza la función, por ello, la salida del ejemplo anterior será 0 y no nos mostrará toda la iteración de la función.

Para hacer que esta función sea un generador debemos hacer uso de la palabra reservada "yield" que lo que hace es suspender de forma momentánea la ejecución de la función, esto para retornar un objeto, una vez el objeto haya sido retornado, la función podrá reanudarse en el punto donde se detuvo.

```
def pares():
    for numero in range(0, 100, 2):
        #return numero
        yield numero

print(pares())
```

Si ejecutamos esta función ya no obtendremos 0, obtendremos un objeto de tipo generador que podremos obtener sus valores a demanda.

Esto lo podemos ver con el siguiente código.

```
def pares():
    for numero in range(0, 100, 2):
        #return numero
        yield numero

print(pares())

for par in pares():
    print(par)
```

La palabra reservada "yield" nos permite retornar valores sin que la función finalice, únicamente pausando su ejecución para que posteriormente pueda reanudarse desde el punto donde se quedo.


### Conclusión 

Cuando trabajamos con generadores a su vez estamos trabajando con un "Lazy iterator" es decir una iteración perezosa pudiendo obtener los valores del generador a demanda.