# Clase 26 - Curso de Python - Índices de tuplas

## Notas de clase


### Introducción
Al igual que con las listas se trabajará con los índices en las tuplas, esto para obtener los valores de los elementos almacenados.


### Índices de tuplas


Cada elemento de la tupla le corresponde un índice (posición) mediante la cual podemos acceder al valor del elemento almacenado en la tupla.

`cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')`

Los índices inician en 0 hasta el número de longitud de elementos que la tupla almacene. Para acceder a un valor de un elemento basta con imprimir la variable de la tupla usando los corchetes e indicando la posición como se realizaba en las listas.

`print(cursos[0])`

Al igual que las listas contamos con la lectura negativa de las posiciones lo que nos permite acceder al último elemento de la tupla usando -1 como índice.


Con las tuplas seremos capaces de generar sub tuplas y podemos seguir la mismas sintaxis para dar un inicio, un final e incluso saltos como lo hacíamos en las listas.

`sub_tupla = cursos[0:3]`
`print(sub_tupla)`

Esta tupla cuenta con los 3 elementos iniciales.


### Conclusión 

De esta forma accedemos a cada uno de los elementos dentro de la tupla, mediante índices positivos o negativos además podemos aplicar la misma sintaxis que las listas para crear sub tuplas.