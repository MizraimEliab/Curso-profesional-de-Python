# Clase 29 - Curso de Python - Zip

## Notas de clase


### Introducción
Ahora se trabajará en el proceso contario a desempaquetar los elementos de una tupla, mediante el uso de una función que nos ayudaran a combinar valores de diferentes estructuras de datos.


### Zip

Se puede combinar los elementos de diferentes estructuras de datos, por ejemplo, los valores de una lista y una tupla, para ello se hará uso de la función "zip()" pasándole como argumentos las estructuras que queramos comprimir.

`lista = [1, 2, 3, 4, 5]`
`tupla = (10, 20, 30, 40, 50)`
`resultado = zip(tupla, lista)`
`print(resultado)`

La función "zip()" nos retorna un objeto de tipo zip con el cual podemos trabajar por ejemplo convirtiendo dicho objeto en una tupla con la función "tuple()" como se muestra en el siguiente ejemplo.

`print(tuple(resultado))`

Esto nos imprime una tupla con sub tuplas dentro con la combinación de los elementos de nuestra lista y nuestra tupla inicial.

Para esto hay que saber que podemos utilizar solo listas, solo tuplas o como el ejemplo una lista y una tupla.

`lista_2 = [100, 200, 300, 400, 500]`
`resultado = zip(lista, tupla, lista_2)`
`print(tuple(resultado))`

Con esto se comprende que podemos pasar n cantidad de listas o tuplas para la función "zip()" y que esta se encargará de comprimir nuestros valores para que los podamos utilizar en otra parte de nuestro programa.

Si alguna estructura no cuenta con la misma cantidad de elementos simplemente cuando se genere la tupla los elementos adicionales no serán tomados en cuenta cuando se genere la tupla comprimida ya que la combinación debe ser exacta.


### Conclusión 

Es importante recalcar que las estructuras deben contar con la misma longitud para que al generar la tupla final los valores a comprimir sean tomados en cuenta ya que de los contrario los valores adicionales de las estrcuturas no serán tomados en cuenta.