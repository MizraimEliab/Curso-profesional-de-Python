# Clase 30 - Curso de Python - Strings con listados

## Notas de clase


### Introducción
Los strings cuentan con una gran variedad de métodos con los que podemos trabajar, se revisarán algunos, sin embargo, existen un gran número de métodos con los que podemos trabajar los strings en Python.


### Strings con listados


Los primeros métodos a revisar es el de "split()" y "join()" donde el método "split()" nos permite generar una lista a partir de un string y por su parte el método "join()" nos permite generar un string a partir de una lista.

`lenguajes = 'Python Ruby Java Rust C++ C'`

`listado_lenguajes = lenguajes.split()`
`print(listado_lenguajes)`
`['Python',  'Ruby',  'Java',  'Rust',  'C++',  'C']`

Es importante mencionar que el método "split()" va a dividir el texto usando los espacios que encuentre en este, donde cada espacio denota un nuevo elemento de la lista.

Si colocamos por ejemplo guione medios en lugar de espacios en el string obtendremos con el método "split()" una lista de un solo elemento que contendrá todo el string debido a que no existen espacios y no hay forma de dividirlo por defecto.

Si necesitamos que nuestro string quede divido en una lista y el string no contiene espacios y esta separado por otro carácter como guion medio o guion bajo podemos pasarle el signo como argumento a la función "split()" para indicarle que divida basándose en ese signo.

`lenguajes = 'Python-Ruby-Java-Rust-C++-C'`
`listado_lenguajes = lenguajes.split('-')`
`print(listado_lenguajes)`
`['Python',  'Ruby',  'Java',  'Rust',  'C++',  'C']`

Ahora, opcionalmente al método "split()" le podemos pasar un segundo argumento para indicar el número de divisiones que queramos hacer a partir del carácter indicado.

`listado_lenguajes = lenguajes.split('-', 2)`
`['Python',  'Ruby',  'Java-Rust-C++-C']`

Usualmente el número de divisiones no se indica comúnmente, sien embargo, es bueno conocer que tenemos la posibilidad de  hacer ese ajuste con nuestra lista generada.

Ahora veremos el método inverso a "split()", el método "join()" que nos permite generar un string a partir de los valores de una lista, esto se logra haciendo uso comúnmente de un espacio de un string inicial, "join()" unirá los elementos con el carácter que indiquemos en el string inicial y el método "join()" retornará un string que podemos almacenar en una variable.

`lenguajes = ['Python', 'Ruby', 'Java', 'Rust']`
`string_lenguajes = ' '.join(lenguajes)`
`print(string_lenguajes)`
`Python Ruby Java Rust`

Como se puede observar en el ejemplo, el método "join()" recibe como argumento una lista para poder generar nuestro string.

En el caso de "join()" la unión del carácter es similar al método "split()" dependiendo del signo a usar se generará nuestro string unido con ese signo.


### Conclusión 

Con el método "split()" y el método "join()" podemos generar una lista a partir de un string y viceversa, generar un string a partir de una lista, con las funciones podemos trabajar nuestros listados que de alguna manera llegan en string o queremos hacer una lista para organizar mejor la información a partir de un string.