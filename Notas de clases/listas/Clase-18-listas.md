# Clase 18 - Curso de Python - Listas

## Notas de clase


### Introducción
En un lista todos los elementos almacenados en ella tienen una posición asignada, a esta posición la conoceremos como índice y mediante un índice seremos capaces tanto de obtener como de actualizar un elemento de nuestra lista. 


### Listas

`lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']`

Para iniciar se tiene la lista de 5 elementos de tipo string y primeramente vamos a conocer como obtener un elemento especifico de la lista, para ello haremos uso de una variable para guardar nuestro primer string de la lista.

`primer_curso = lista_cursos[0]`
`print(primer_curso)`
`Python`

Como se puede observar en el ejemplo anterior hacemos uso de los corchetes seguido del nombre de la lista para acceder al índice del elemento de nuestra lista.

De esa manera podemos obtener cualquier elemento de nuestra lista simplemente conociendo y accediendo a su índice.

`segundo_curso = lista_cursos[1]`
`print(segundo_curso)`
`Django`

Es importante mencionar que se pueden trabajar los índices con números negativos, por ejemplo basándonos en nuestra lista para obtener el último elemento de nuestra lista podemos hacer uso del índice 4 o bien del índice -1, por default la listas se leen de izquierda a derecha del ínidice 0 en adelante, sin embargo, cuando hacemos uso de índices negativos la lectura de la lista se hará de derecha a izquierda y por ende los índices van a cambiar iniciando por el -1 hasta el número de elementos en la lista en negativo, es decir, -1, -2, -3, -4. 

La razón por la cual al imprimir la lista en la posición -1 se obtiene su último elemento es porque la lectura de la lista de hacer de derecha a izquierda iniciando por el último elemento de la lista.


Regularmente siempre es recomendable trabajar con números positivos, es decir, lectura de la lista de izquierda a derecha exceptuando el último elemento, el penúltimo o el antepenúltimo.

Finalmente si nosotros intentamos obtener un índice que no exista en la lista obtendremos un error.

`IndexError: list index out of range`

Este error que muestra Python significa que el índice buscado no se encuentra dentro del rango de nuestra lista y por lo tanto no puede ser obtenido y esto ocurre en las 2 formas de lectura de la lista.


### Conclusión 

Dentro de la listas cada elemento tiene un índice que podemos usarlo para obtener el valor del elemento y existen 2 tipos de lecturas que podemos usar para el manejo de los índices y obtención de valores siempre y cuando los índices se encuentren dentro del rango de nuestra lista y no lo excedamos ya que si lo hacemos obtendremos un error al ejecutar el programa.