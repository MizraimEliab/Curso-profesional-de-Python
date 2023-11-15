# Clase 28 - Curso de Python - Desempaquetado

## Notas de clase


### Introducción
Ya conocemos que podemos crear múltiples variables con sus valores en una misma línea de código, esto con la finalidad de ahorrar líneas de código siempre que se pueda y se preste la ocasión.


### Desempaquetado

Con las tuplas también podemos escribir una sintaxis parecida y podemos manejar de esta manera nuestros elementos.

`uno, dos, tres, cuatro = 1, 2, 3, 4`
`numeros = (1, 2, 3, 4)`

Esto se logra imprimiendo nuestras variables pero ahora asignadas a la tupla como tal ya que Python esta asignando cada variable con el valor de la tupla correspondiente, obteniendo el mismo resultado de solamente imprimir las variables.

`uno, dos, tres, cuatro = numeros`
`print(uno)`
`print(dos)`

Esta manera es una forma más legible de poder asignar valores de la tupla en variables ya que representa los mismo como si asignáramos el valor de a la variable mediante la tupla con su índice.

`uno = numeros[0]`
`dos = numeros[1]`
`print(uno)`
`print(dos)`

Cuando se trabaja con tuplas esta manera es la forma en la que se descomprime o desempaqueta una tupla para poder trabajar con los valores de la tupla con variables.

Ahora que pasa ni nosotros no conocemos de antemano la cantidad de elementos de nuestra tupla, es decir, desconocemos la longitud de la tupla.

`numeros = (1, 2, 3, 4, 5)`
`uno, dos, tres, cuatro = numeros`

Al ejecutar el programa vamos a obtener un error "ValueError: too many values to unpack" que nos indica que existen demasiados valores para desempaquetar.

Este error lo podemos solucionar si colocamos un asterisco como prefijo en nuestra última variable para indicarle a Python a partir de la variable con el prefijo se almacenarán los elementos restantes de la tupla.

`uno, dos, tres, *resto_valores = numeros`
`print(resto_valores)`
`[4, 5]`

Como se puede ver en la salida se nos regresa una lista en la variable "resto_valores" con todos los demás elementos de la tupla, es decir, todos los valores que no tengan su propia variable serán almacenados en una lista.

El asterisco es muy importante al trabajar con listas ya que es comúnmente usado en listas dentro de funciones, etc. Siempre que se vea un asterisco hay relación con listas.

Si nosotros queremos que Python ignore los valores restantes de una tupla en lugar de crear nuestra variable con el prefijo de asterisco podemos agregar en lugar de la variable un guion bajo para decirle a Python que los valores restantes de la tupla simplemente los queremos ignorar.

`uno, dos, tres, *_ = numeros`

Es recomendable que si no trabajaremos con todos los elementos de la tupla simplemente omitamos estos elementos y no creemos una variable que ocupe espacio en memoria.

Para complicar más el escenario que pasa si queremos omitir los valores siguientes a x posición pero si deseamos los últimos valores de la tupla, para ello podemos realizar lo siguiente.

`numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)`
`uno, dos, tres, cuatro, *_, nueve, diez = numeros`
`print(nueve)`
`print(diez)`

Como podemos ver si que colocamos variables para los últimos 2 elementos de la tupla, esto hará que Python los tome en cuenta y nos guarde nuestros valores en nuestras variables.

Es importante notar como Python sabe a través de las variables cuales valores queremos desempaquetar y cuales no.

El guion bajo nos ayuda a decirle a Python que queremos omitir el valor y no hay necesidad de crear una variable, por ello en cualquier posición podemos agregar el guion bajo y Python omitirá ese elemento.

`uno, _, tres, cuatro, *_, nueve, diez = numeros`

En el ejemplo anterior se omite el valor del índice 1 de la tupla.


### Conclusión 

El tema de desempaquetado como se observa es muy interesante debido a que dependiendo de la forma en la que trabajemos nuestra tuplas, variables y símbolos podemos obtener diferentes resultados para diferentes aplicaciones prácticas.