# Clase 40 - Curso de Python - Llaves, Items y valores

## Notas de clase

### Introducción
En ocasiones tendremos la necesidad de conocer que llaves, valores o llaves y valores tenemos en nuestro diccionario, afortunadamente tenemos 3 métodos que nos ayudan con estas tareas.

### Llaves, Items y valores

Los métodos son "keys()", "values()" y "items()" estos métodos son de consulta y como su nombre lo indican permiten conocer las llaves, los valores y todo los items de un diccionario.

Vamos revisando uno por uno.

Para revisar las llaves de un diccionario haremos uso del método "keys()" que nos retornará un objeto con todas las llaves de un diccionario dado.

`diccionario = {'a': 1, 'b':2, 'c':3, 'd':4}`
`llaves = diccionario.keys()`
`print(llaves)`

El objeto es de tipo "dict_keys"  objeto que podemos convertir en una tupla.

`llaves = tuple(diccionario.keys())`

Convertirlo en una tupla es una forma más simple y efectiva de trabajar con las llaves.

Ahora obtendremos los valores del diccionario  aplicando la misma syntaxis que con el método de "keys()" pero ahora haciendo uso del método "values()".

`valores = diccionario.values()`
`print(valores)`

Esto nos retornará un objeto de "dict_values" que de igual manera podemos convertir ese objeto en tupla para trabajarlo mejor.

`valores = tuple(diccionario.values())`

Ahora pasamos con los items del diccionario que es misma syntaxis que los métodos anteriores.

`elementos = diccionario.items()`
`print(elementos)`

Esto nos retorna un objeto de tipo "dict_items" con las llaves y valores del diccionario donde podemos hacer lo propio y convertirlo en una tupla.

`elementos = tuple(diccionario.items())`

Es importante mencionar que los objetos que retornan cada uno de los métodos los harán en el mismo orden del diccionario tanto para llaves y valores.


### Conclusión 

Con estos métodos es como podemos conocer los valores, llaves y todos los items que se encuentran almacenados en un diccionario.

Los objetos resultantes los podemos transformar en tuplas para trabajar mejor los valores.