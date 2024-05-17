# Clase 47 - Curso de Python - Asignar valores mediante operadores lógicos

## Notas de clase

### Introducción
Algo interesante del operador lógico "or" es que a través de él seremos capaces de asignar valores  a nuestra variables.

Funciona de la siguiente manera, Python evalúa cada una de las opciones al utilizar el operador lógico "or" y va a asignar a la variables el primer valor Verdadero con el cual se encuentre.

### Asignar valores mediante operadores lógicos

Revisemos un ejemplo, dada una variable que contiene un nombre podemos asignar el valor a dicha variable siempre y cuando una opción sea verdadera, en este caso como se muestran strings como valores y no string vacíos, Python lo interpretará como verdadero en su primer nombre.

```
nombre = 'Alex' or 'Alan'
Alex
```
Pero si colocamos el primer string vacío Python lo tomará como falso por lo tanto imprimirá el otro nombre.

```
nombre = '' or 'Alan'
Alan
```

Este ejemplo se mostro con valores de tipo strings, sin embargo, no estamos limitados a solo estos tipos de datos ya que podemos realizar este ejemplo usando otros tipo como enteros, flotantes, listas, etc.

Vemos otro ejemplo.

```
nombre = '' or 0 or [] or True
True
```

En este ejemplo anterior se muestra la variable boolean True debido a que las demás Python las interpreta como falso por ello se le asigno ese valor a la variable.

El asignar valores mediante el operador lógico "or" resulta de mucha utilidad cunado queremos que una variable tome el valor de otra variable u otra dependiendo de un caso, esto se puede arreglar con una condicional, sin embargo, es más optimo y simple de leer usando la syntaxis de los ejemplo mediante el uso del operador "or".

```
listado = []
nombre = 'Dante'

if listado:
    nombre = listado
else:
    nombre = nombre

print(nombre)

```

En este ejemplo el resultado sería "Dante" debido a que la lista vacía se considera un valor falso.

La reducción usando el operador "or" quedaría de la siguiente manera.

```
nombreN = nombre or listado
Dante
```

### Conclusión 

Para Python una lista vacía, una tupla vacía, un diccionario vacío, un 0, un 0.0, un string vacío y un False son considerados como valores Falsos y en base a esa asignación Python tomará dicho valor para evaluarlo con el operador lógico "or".