# Clase 17 - Curso de Python - ¿Qué son las listas?

## Notas de clase


### Introducción
Las listas en Python son una estructura de datos, es decir es un tipo de dato que nos permite manejar grandes cantidades de otros datos.


### ¿Qué son las listas?

Comenzando creando nuestra primera lista para ejemplificar mejor el concepto, existen 2 formas de crear una lista en Python, la primer forma es mediante el uso de la función "list" que puede ser asignada a una variable para crear nuestra lista, la segunda opción es trabajar con corchetes que se asignan a nuestra variable lista, ambas formas son lo mismo.

`lista = list()`
`lista = []`


Las listas permiten almacenar otros tipos de datos ya sean strings, enteros, reales, booleans, tuplas, diccionarios, etc. Para ello cuando creamos nuestra lista podemos colocar dentro de los corchetes de nuestra lista todos aquellos elementos los cuales queramos se almacenen dentro de la lista.

`lista = ['String', 10, 15.6, True]`
`print(lista)`

De esta manera podemos crear una lista que inicie almacenando diferentes elementos, simplemente dentro de los corchetes agregamos todos los elementos de la lista separados por comas.

Cada uno de los elementos dentro de la lista obligatoriamente les corresponde un índice (posición) dentro de la lista y los índices en Python inician en 0, entonces...

`0, 1, 2, 3`
`lista = ['String', 10, 15.6, True]`

A pesar de que las listas nos permiten almacenar diferentes valores con diferente tipo de dato lo aconsejable es que guardemos las listas lo hagamos con elementos de un solo tipo de dato, por ejemplo puros enteros.

`lista = [10, 20, 30, 40]`

De esta manera estaremos estandarizando nuestra forma de codificar.

### Conclusión 

Las listas nos ayudan a almacenar diferentes valores de diferentes tipos de datos, esto puede ser mu útil a la hora de maejar grandes cantidades de datos en nuestros programas además de poder organizar dichos datos y conocerlos de una manera más sencilla.