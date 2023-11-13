# Clase 23 - Curso de Python - Index

## Notas de clase


### Introducción
Ya que hemos conocido los diferentes métodos que podemos aplicar a nuestras listas en Python, seguramente necesitemos conocer más sobre los elementos de nuestra lista.


### Index

Ya que hemos confirmado que nuestro elemento se encuentra en la lista mediante la expresión con la palabra reservada "in" y necesitamos conocer además del elemento, el ínidice en que este se encuentra podemos hacer lo siguiente.

`print(5 in lista)`
`index =  lista.index(5)`
`print(index)`

El método "index()" nos ayuda a conocer el que índice se encuentra un valor ya que este retorna el índice del elemento que nosotros le pasemos como argumento a la función como se puede ver en el ejemplo anterior.

Algo importante a mencionar es que la función "index()" va a retornar el primer valor encontrado, es dcir, que si nuestro elemento se encuentra múltiples veces en nuestra lista el método "index()" retornará el índice del primer elemento de la lista.

Si intentamos obtener el índice de un elemento que no se encuentre en la lista mediante el método "index()" obtendremos un error.

`ValueError: 500 is not in list`


### Conclusión 

Cuando hemos identificado que un elemento existe en nuestra lista con toda confianza podemos hacer uso del método "index()" para conocer el índice del elemento siempre tomando en cuenta que nuestro elemento puede estar múltiples veces en nuestra lista.