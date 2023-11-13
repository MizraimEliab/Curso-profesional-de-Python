# Clase 22 - Curso de Python - Métodos de listas

## Notas de clase


### Introducción
Podemos trabajar de diferentes formas con las listas y podemos hacer diferentes operaciones con los elementos de las listas, por ejemplo cuando tenemos elementos de un solo tipo de dato.


### Métodos de listas

Ya que se mencionó que cuando tenemos una lista llena de elementos de un solo tipo de dato podemos hacer operaciones con los elementos vamos a ver el caso cuando se tienen puros valores enteros de manera desordenada.

`lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]`

Si queremos ordenar los elementos de la lista tenemos 2 opciones, la primera opción es implementar un algoritmo de ordenamiento como por ejemplo el algoritmo de burbuja, etc. La segunda manera y la más simple es hacer uso del método "sort()" de Python para lograrlo.

`lista.sort()`

El método "sort()" por default ordenará la lista de forma ascendente, es decir, de menor a mayor. Podemos hacer que el ordenamiento se haga a la inversa, es decir, de mayor a menor en forma descendente, para ello le pasamos un parámetro a la función "sort()" indicando que se cambiará el orden, el parámetro es el siguiente.

`lista.sort(reverse=True)`

Cuando trabajamos con listas con elementos numéricos en Python regularmente necesitaremos conocer el menor y mayor valor dentro de nuestra lista, esto lo podemos lograr ordenando la lista y luego accediendo a los índices, en este caso al primer índice para el valor menor y al último índice para el valor mayor , sin embargo, en Python tenemos funciones para obtener estos valores.

Tenemos la función "min()" y la función "max()" para conocer estos valores solamente pasándoles como parámetro nuestra lista.

`print(min(lista))`
`print(max(lista))`


Para finalizar también podemos conocer si un elemento se encuentra dentro de nuestra lista o no, esto lo podemos lograr mediante la palabra reservada "in" y con una expresión podemos saber si un elemento se encuentra en la lista.

`print(10 in lista)`

L expresión nos regresa un valor boolean donde verdadero significa que el elemento se encuentra en la lista y falso si no se encuentra el elemento en la lista.

Esta expresión la podemos negar para confirmar que un elemento no se encuentre en la lista, esto lo podemos hacer con la palabra reservada "not".

`print(11 not in lista)`


### Conclusión 

Se puede trabajar de diferentes maneras con la listas, sin embargo, Python nos ayuda con algunos métodos para realizar tareas comunes que podemos hacer con frecuencia de una manera simple y práctica sin la necesidad de escribir más líneas de código.