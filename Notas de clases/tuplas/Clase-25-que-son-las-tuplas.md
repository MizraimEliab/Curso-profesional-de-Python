# Clase 25 - Curso de Python - ¿Qué son las tuplas?

## Notas de clase


### Introducción
Ahora se trabajará con otra estructura de datos, en este caso las tuplas, las tuplas son muy parecidas a las listas y nos permiten almacenar diferentes tipos de datos, string, enteros, flotantes, listas, etc.

La principal diferencia entre las listas y las tuplas es que las tuplas son inmutables, es decir, una vez se defina una tupla así se quedará por el resto del programa ya que nos seremos capaces de modificar los elementos de una tupla ni tampoco la longitud de esta.

En la lista podemos añadir y eliminar elementos , en las tuplas esto no es posible.


### ¿Qué son las tuplas?


Si nosotros creamos una tupla que almacene 10 strings, estos 10 strings se quedarán presentes por todo el programa y solo podremos consultarlos.

Para crear una tupla en Python basta con asignar paréntesis a nuestra variable tupla.

`tupla = ()`
`print(tupla)`
`( )`

Esta ya es una tupla y lo podemos verificar mediante la función "type()" sin embargo, en una tupla vacía, lo común, es definir con los elementos que queremos almacenar dentro de los paréntesis de la tupla separando los elementos por una coma.  

`tupla = ('String', 10, 15.4, True, [1,2,3], (4, 5, 6))`

Como se puede observar al igual que la lista podemos almacenar diferentes tipos de datos incluidas otras tuplas sin ningún problema.

Cada elemento de la tupla le corresponde un índice, es decir, una posición dentro de la tupla y los índices inician en 0. Mediante los índices seremos capaces de consultar los elementos almacenados en la tupla.

Una diferencia importante sobre las tuplas es que son mucho más rápidas al momento de consultar elementos se refiere en comparación con las listas ya que las tuplas al ser objetos inmutables son almacenadas en memoria dentro de un espacio de lectura especial.


### Conclusión 

Las tuplas son perfectas estructuras de datos para que podamos consultar sus valores de forma rápida ya que al ser objetos inmutables nos permite obtener la información que almacenan rápidamente. 