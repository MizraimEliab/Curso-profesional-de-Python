# Clase 19 - Curso de Python - Actualizar elementos

## Notas de clase


### Introducción
Con ayuda de los índices en las listas podemos actualizar un elemento en concreto. 


### Actualizar elementos


Para actualizar el elemento de una lista vamos a tomar como ejemplo la lista previamente mencionada y se hará una reasignación del elemento basandonos en la posición -1 que representa el ínidice del último valor.

`lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']`
`lista_cursos[-1] = 'Rust'`

Con el ejemplo anterior ya hemos actualizado el último elemento de la lista y cambiamos 'Java' por 'Rust'.

Ya que actualizamos el elemento si deseamos conocer los valores de la lista obtendremos lo siguiente.

`lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust']`


### Conclusión 

Dentro de la listas cada elemento tiene un índice que podemos usarlo para obtener el valor del elemento y existen 2 tipos de lecturas que podemos usar para el manejo de los índices y obtención de valores siempre y cuando los índices se encuentren dentro del rango de nuestra lista y no lo excedamos ya que si lo hacemos obtendremos un error al ejecutar el programa.