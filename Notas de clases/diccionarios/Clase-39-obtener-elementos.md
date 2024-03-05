# Clase 39 - Curso de Python - Obtener elementos

## Notas de clase

### Introducción
Cada diccionario al contar con elementos podemos acceder a ellos ya que al final del día son datos almacenados en una estructura de datos.

### Obtener elementos

Ya que conocemos la estructura de los diccionarios, es decir sabemos que son una estructura de clave-valor podemos hacer uso del dato de la clave para acceder al valor que la clave contiene.

En el siguiente ejemplo se define un diccionario  ya con valores y se almacena en una variable nueva el valor de una clave.

`diccionario = {'a': 1, 'b':2, 'c':3, 'd':4}`
`valor = diccionario['d']`
`print(valor) # 4`

De esa manera es como podemos obtener los valores almacenados en las claves de un diccionario, haciendo uso de los corchetes seguidos del nombre de la variable del diccionario y agregando dentro de los corchetes el nombre de la clave.

Nosotros podremos obtener los elementos de una clave dentro de un diccionario siempre y cuando esta clave exista, ya que si tratamos de acceder a una clave inexistente obtendremos un error por consola de tipo KeyError.

Para evitar el error de tipo KeyError podemos hacer uso de la palabra reservada "in" ya que esta palabra nos permite conocer si un elemento se encuentra o no dentro de una estructura de datos.

Podemos evaluar la expresión que nos retornará un valor boolean para conocer si una clave existe en el diccionario o no.

`print('a' in diccionario) # True`

La expresión anterior puede ser condicionada y manejar de una manera más completa los datos.

Podemos hacer uso del método "get()" de los diccionarios para obtener el valor de una clave de manera segura, este método espera como argumento en nombre de la clave de la cual queremos obtener su valor.

`valor = diccionario.get('d')`
`print(valor) # 4`

Si intentamos obtener el valor de una clave que no existe dentro del diccionario con el método "get()" el resultado será "None" y no obtendremos el error por clave que se presentaba con el uso de los corchetes.

`valor = diccionario.get('z')`
`print(valor) # None`

"None" en Python es la ausencia de valor (equivalente a un valor nulo en otros lenguajes).

El método "get()" opcionalmente puede recibir un segundo argumento que representaría el valor "default" al retornar en caso de que la clave buscada en el primer argumento no exista dentro del diccionario. El valor "default" puede ser de cualquier tipo.

Si la clave si existe se ignora el segundo argumento y se retorna el valor de la clave.

`valor = diccionario.get('z', 'La llave no existe')`
`print(valor) # 'La llave no existe'`


El método "get()" tiene una contraparte que es el método "setdefault()" que este último nos permitirá obtener el valor de una clave, en dado caso la clave no exista se procederá a añadir su respectivo valor al diccionario.

`valor = diccionario.setdefault('e', 5)`
`print(valor) # 5`

Como se muestra en el ejemplo ya que no existe la clave "e" se le agregará a esa nueva clave el valor 5 dentro del diccionario.



### Conclusión 

De esas maneras es como podemos obtener valores de los diccionarios, mediante el uso de los corchetes o bien haciendo uso del método "get()" o "setdefault()" para una obtención segura de los datos cuando no se encuentran presentes las claves.