# Clase 54 - Curso de Python - Parámetros opcionales

## Notas de clase

### Introducción
Algo interesante de Python es que a diferencia de otros lenguajes de programación dentro de las funciones podemos tener parámetros opcionales y para ello se afinan valores por defecto a dichos parámetros.

### Parámetros opcionales

Vamos a revisar los parámetros opcionales mediante un ejemplo de una función que nos permita calcular el área de un circulo.

```
def area_circulo(radio, pi):
    return pi * (radio ** 2)

resultado = area_circulo(10, 3.14)
print(resultado)
```

Esta función esta correcta y nos devolverá el valor deseado de área de un circulo, sin embargo, los parámetros de la función son obligatorios de tal manera que si alguno se elimina Python marcará un error.

Para esta función conocemos que la variable "pi" es una constante y sabemos que su valor no cambiará por lo tanto se puede establecer su valor por defecto desde la función haciendo uso del signo "=" y el valor para que al momento de llamar la función sea opcional indicar un valor para la variable "pi".

```
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)

resultado = area_circulo(10)
print(resultado)
```

Los valores por defecto se leen de derecha a izquierda y es importante mencionar que cuando establecemos un valor por defecto en un parámetro dentro de una función por convención de la comunidad Python es recomendable no usar espacios con el signo "=".

Si no se respetan el orden de los argumentos en la función obtendremos un error de argumento, ya que las variables que tengan valor por defecto deben encontrase a la derecha.

El que una variable tenga un valor por defecto no significa que este no pueda ser cambiado, simplemente se volvería a indicar un nuevo valor en la ejecución de la función.

```
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)

resultado = area_circulo(10, 3.141592)
print(resultado)
```

Esto hace que aunque la variable tenga un valor por defecto, este valor sea sustituido por el que indicamos en ejecución.

En Python podemos trabajar con nombre de los parámetros en la ejecución de la función y lo interesante de esto es que podemos hacerlo sin importar la posición del parámetro debido a que Python reconoce a que parámetro se esta referenciando.

```
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)

resultado = area_circulo(pi=3.141592, radio=10)
print(resultado)
```

### Conclusión 

En Python los parámetros opcionales nos ayudan a establecer valores que no cambiarán con opción a actualizarlos o no en base a las necesidades de nuestro programa lo que permite un código más limpio, estructurado y funcional.