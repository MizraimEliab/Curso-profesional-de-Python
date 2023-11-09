# Clase 20 - Curso de Python - Sublistas

## Notas de clase


### Introducción
Cuando trabajamos con las listas en Python tenemos la posibilidad de crear sublistas además de hacer una estructura de datos más compleja para trabajar, esto permite que tengamos escenarios más interesantes y complejos a la hora de trabajar con las listas.


### Sublistas

Para crear las sublistas se requiere que nos apoyemos nuevamente de los índices de las listas para que mediante ellos podamos manejar un rango concreto que tendrá nuestra sublista, revisemos un ejemplo.


`lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']`
`sub_lista = lista_cursos[0:3]`
`print(sub_lista)`
`['Python', 'Django', 'Flask']`

Al imprimir nuestra variable de sublista podemos notar que el resultado fue una lista solamente con los 3 elementos iniciales y de la lista original debido a que la sublista la declaramos con el índice inicial 0 luego indicamos doble el signo de dos puntos y finalmente el ínidice final de elementos recordando que el índice final no será tomado en cuenta, si no, que llegará a 3 elementos a partir del índice 0, es decir llegará hasta el índice 2.

Entonces la estructura para la sublista sería tener un índice inicial, después agregar dos puntos para indicar un rango y finalmente agregar el índice final que no será tomado en cuenta.

`# sub_lista[inicial:final] `

Ahora ¿Qué pasa cuando se agrega un índice final que no existe?, ¿marcará error?. Cuando se tiene un índice final que no existe y se imprime la sublista no se retorna un error ya que Python tomará todos los elementos a partir del índice inicial y con ellos generará la sublista agregando así para este caso todos los elementos de la lista.

Esto también los podemos lograr omitiendo el ínidice final ya que tomará los últimos elementos a partir del índice inicial.

`sub_lista = lista_cursos[0:]`

Lo anterior es particularmente usado y útil cuando se desea obtener los últimos elementos de la lista, pero, ¿Qué pasa si queremos hacer lo inverso y obtener los primeros elementos?.

Para obtener los primeros elementos de la lista podemos hacer uso del índice final donde haremos alución al índice final donde vamos a terminar la lista, por ejemplo vamos a indicarle a Python que vamos a generar una sublista con los primeros 4 elementos de la lista.

`sub_lista = lista_cursos[:4]`
`print(sub_lista)`
`['Python', 'Django', 'Flask', 'Ruby']`

Como podemos observa el último número del índice no será tomado en cuenta.

Existe la posibilidad de crear una sublista con saltos en los elementos de la lista original y esto lo podemos lograr agregando un tercer valor al rango de nuestra sublista.

Para hacer los saltos tendríamos el siguiente ejemplo donde el número 2 que es el tercer valor en nuestro rango indica los saltos a partir de los cuales se va a generar nuestra lista.

`sub_lista = lista_cursos[1:4:2]`
`print(sub_lista)`
`['Django', 'Ruby']`

En el ejemplo anterior lo que se esta haciendo es saltar desde el índice 1 de 2 elementos en 2 elementos, por ello obtuvimos el resultado anterior.

Los saltos son opcionales y se usan para personalizar más nuestra sublista ya que no es un valor requerido para crear nuestra sublista.

Es importante mencionar que los valores de nuestro rango tanto el índice inicial y final también son opcionales y en caso de que no se agreguen solamente se hace la sublista con todos los elementos.

`sub_lista = lista_cursos[:]`
`print(sub_lista)`
`['Python', 'Django', 'Flask', 'Ruby', 'Java']`

Si realizamos saltos con números negativos se invierten los elementos de nuestra lista original.

`sub_lista = lista_cursos[::-1]`
`print(sub_lista)`
`['Java', 'Ruby', 'Flask', 'Django', 'Python']`


### Conclusión 

En Python podemos crear sublistas a partir de una lista que tengamos en nuestro código apoyándonos de los índices y un rango establecido por el signo de 2 puntos para la creación de nuestra sublista, sin embargo, nuestros índices de apoyo dentro del rango son opcionales, es decir que el índice inicial, final y paso se pueden omitir para una mejor personalización de nuestra sublista.

Dentro del rango para la creación de nuestra sublista dependerá el uso de nuestros índices según las necesidades de nuestro programa.