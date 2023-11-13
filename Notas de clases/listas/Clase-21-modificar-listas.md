# Clase 21 - Curso de Python - Modificar listas

## Notas de clase


### Introducción
En Python es posible modificar las listas añadiendo o quitando elementos de ellas y para ello nos apoyaremos de un par de métodos.


### Modificar listas

Lo primero que podemos hacer para modificar una lista es añadiendo elementos para ello nos apoyaremos del método "append" ya que este método nos permite añadir nuevos elementos al final de nuestra lista.

`lista_cursos.append('Rust')`

En este caso lo que estaos haciendo es agregar el elemento 'Rust' al final de nuestra lista. Este ejemplo muestra un string nuevo para añadir pero tu puedes agregar cualquier objeto.

Al ir agregando elementos a nuestra lista la longitud de aumentará es por ello que si necesitamos conocer la longitud podemos hacer uso de la función "len()" y pasarle como parámetro nuestra lista.
 
`print(len(lista_cursos))`

Con la función "len()" podremos conocer el número de elementos que contiene nuestra lista. Con la función "append()" podemos agregar cualquier tipo de dato a nuestra lista, sin embargo, hay que recordar que debemos mantener en la medida de lo posible valores de un solo tipo de dato en nuestras listas.

Ahora que pasa cuando queremos añadir un nuevo elemento en un índice en particular, para ello, se hace uso del método "insert()" este método nos permite añadir un elemento a la lista a partir de un índice en concreto. El método recibe 2 argumentos, el primero es el ínidice donde se agregara el valor y el segundo es el valor.

`lista_cursos.insert(0, 'C#')`

Cuando se hace uso de la función "insert()" al indicar el índice si este se encuentra ocupado por otro elemento dentro de la lista, el elemento que ya ocupaba el índice se recorre de ínidice junto a los elementos que seguían de él, esto se hará siempre con todos los elementos al usar la función "insert()".


Podemos extender nuestra lista, esto quiere decir que podemos hacer nuestra lista aún más grande a partir de otra lista.

Para ello veremos el siguiente ejemplo.

`lista_cursos_2 = ['C++', 'C', 'Docker']`

Primero se va a definir una segunda lista y mediante la función "extend()" lograremos extender nuestra lista principal con nuestra segunda lista pasando como parametro nuestra segunda lista.

`lista_cursos.extend(lista_cursos_2)`

Esto añade todos los elementos de la segunda lista a la primera sin que la segunda lista se vea afectada.

Ya que añadimos elementos a nuestra lista también podemos modificarla eliminando elementos de la lista, esto se puede lograr con el método de "remove()" donde por parámetro le pasaremos el valor de la lista que queremos eliminar.

`lista_cursos.remove('C#')`

Al eliminar un elemento de la lista todos los elementos se recorren y los índices se reasignan.

Para poder eliminar un elemento de un índice en especifico podemos hacer uso de la palabra reservada "del" para lograrlo y claramente hay que indicar el índice de la lista.

`del lista_cursos[0]`

Estas son las principales 2 formas para eliminar elementos de una lista.

Finalmente si queremos eliminar todos los elementos de una lista podemos hacer uso del método "clear()" para dejar nuestra lista sin ningún elemento.

`lista_cursos.clear()`
`[ ]`

Para el método "clear()" se debe tener mucho cuidado para evitar perder información.


### Conclusión 

Es posible que vayamos modificando nuestras listas añadiendo o quitando elementos y para esto nos apoyamos de diferentes métodos que Python nos proporciona para ir controlando estas modificación en el tiempo de ejecución de nuestro programa.