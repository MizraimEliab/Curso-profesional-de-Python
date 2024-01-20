# Clase 37 - Curso de Python - ¿Qué son los diccionarios?

## Notas de clase

### Introducción
En Python tenemos diferentes estructuras de datos que nos permiten almacenar diferentes datos de diferente tipo, como por ejemplo las listas, las tuplas y los diccionarios.

Los diccionarios al igual que las listas y las tuplas nos permiten almacenar diferentes tipos de datos, strings, boolean, enteros, flotantes, etc. Los diccionarios son mutables, es decir, podemos modificar su longitud, podemos agregar o quitar elementos y todos los valores almacenados en el diccionario pueden ser modificados.

### ¿Qué son los diccionarios?

Los diccionarios son una estructura de datos de Python que no se rige bajo la regla de los índices, en este caso los valores que se almacenen en un diccionario no corresponden a un índice, si no, a una llave, todos los valores necesita tener una llave y cada llave necesita tener un valor.

Algo a tener en cuenta es cada llave puede ser un objeto inmutable de Python, como un string, un entero, un flotante, etc.

Veamos un ejemplo.

`diccionario = {}`
`diccionario = dict()`

`diccionario = {"total": 55}`
`diccionario = {"total": 55, "descuento": True, "subtotal": 15}`

Como se puede ver en el ejemplo anterior podemos definir un diccionario simplemente haciendo uso de las llaves o bien mediante la función "dict()" ambas formas son correctas.

También podemos observar el uso de la llave-valor ya que vemos que en el ejemplo anterior se usa el string "total" como llave y el valor 55. Con esto le indico a Python que la llave "total" almacena 55.

Si requerimos almacenar nuevos valores basta con separarlos mediante coma como se ve también en el ejemplo.

Los diccionarios son muy versátiles esto quiere decir que podemos tener un diccionario tan variado en llaves y valores como se muestra en el siguiente ejemplo.

`diccionario = {"total": 55, 10: "Curso de Python", (1,2,3): True}`

Comúnmente las llaves serán string pero que sepas que si ocupas almacenar otro tipo de dato como llave lo puedes hacer. Un dato interesante es que se pueden usar clases como llaves.

Los diccionarios te serán muy familiares si has trabajado con la notación JSON, ya que el equivalente a JSON en Python es un diccionario.

Para agregar o modificar algún elemento del diccionario haremos uso de corchetes para indicar la llave y seguido de un signo de igual el valor.

Agregar un elemento
`diccionario["curso"] = "Curso de Python"`
`print(diccionario)`

Modificar un elemento
`diccionario["total"] = 60`
`print(diccionario)`

Acceder a un elemento
`print(diccionario["total"])`

Eliminar un elemento
`diccionario.pop("descuento")`
`print(diccionario)`


Podemos obtener todas las llaves mediante el uso del método "keys()" y todos los valores del diccionario usando el método "values()".

`print(diccionario.keys())`
`print(diccionario.values())`

Y si necesitamos recorrer todas sus llaves como sus valores hacemos uso del método "items()".

`print(diccionario.items())`

También podemos hacer uso del método "get()" que nos permite acceder a un valor a partir de una llave exista o no, ya que si la llave no existe podemos mandar una lista vacía y evita un error y si realmente existe la usa, caso contario a si intentamos acceder a un valor mediante una llave inexistente mediante corchetes donde obtendremos el error de "KeyError".

`print(diccionario.get("total2"), [])`


### Conclusión 

Al igual que con las listas podemos usar operaciones dentro de los valores sin problema.