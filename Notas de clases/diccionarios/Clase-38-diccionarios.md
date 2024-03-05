# Clase 38 - Curso de Python - Diccionarios

## Notas de clase

### Introducción
Añadir y obtener elementos de un diccionario es algo interesante por la versatilidad del uso de las diccionarios y los datos que estos almacenan. 

### Diccionarios

Para ir revisando como agregar y consultar  elementos de un diccionarios tendremos que crear uno y a partir de este se irá agregando información.

`elementos = {}`

Para añadir un elemento a un diccionario basta con que usemos la variable de nuestro diccionario y agregaremos entre corchetes la llave que tomará el diccionario de después de un signo de igual el valor.

Las llaves de un diccionario serán objetos inmutables, es decir, objetos los cuales no pueden modificar su valor en tiempo de ejecución.

`elementos['nombre'] = 'Alan'`
`print(elementos)`
`{ 'nombre': 'Alan' }`

Si nosotros quisieramos conocer la longitud de un diccionario podemos hacer uso del método "len()" dentro de la función "print()" para saberlo.

`print(len(elementos))`

Se pueden añadir la n cantidad de elementos que se requieran al diccionario de diferentes tipos de datos tanto para la llave como para el valor, solamente siguiendo la misma estructura.

Podemos modificar el valor si así lo requerimos en tiempo de ejecución, es decir usando la misma estructura para agregar solamente con la diferencia de cambio de valor.

Python hace lo siguiente si la llave indicada no existe dentro del diccionario entonces la crea junto a su valor, si ya existe dicha llave entonces la actualiza con respecto al valor.

`elementos['nombre'] = 'Dante'`

Si desde que creamos nuestro diccionario definimos algunas llaves con sus valores pero una de las llaves se encuentra repetida Python tomará solamente la última asignación de la llave, es decir tomará solamente una vez la llave con el último valor asignado para esa llave.

`elementos = {'a': 1, 'b': 2, 'c': 3, 'a':4}`
`{'a': 4, 'b': 2, 'c': 3}`

Esto demuestra que Python no permite duplicación de llaves y siempre le asignará el último valor indicado a la llave existente.

Finalmente para consulta de un valor de una llave especifica se hace uso de la función "print()" e agregando el nombre del diccionario y entre corchetes la llave a consultar, si necesitamos conocer todos los valores del diccionario basta con indicar el nombre de la variable.

`print(elementos['nombre'])`
`print(elementos)`



### Conclusión 

A partir de la versión 3.7 de Python los diccionarios conservan el orden con respecto a sus llaves en el cual fueron definidos.
