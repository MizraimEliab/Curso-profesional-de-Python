# Clase 9 - Curso de Python - Tipos de datos

## Notas de clase


### Introducción
En Python nosotros podemos trabajar con diferentes tipos de datos, un tipo de dato es la propiedad de un valor para poder determinar que valores puede tomar.


### Tipos de datos

Comenzamos hablando de 4 tipos de datos que son los más comunes para iniciar en el tema.

	- String
	- Int
	- Float
	- Boolean

El tipo de dato String nos permite representar texto ya sea a través de comillas dobles o comillas simples .

Ejemplo:

`titulo_curso = 'Curso profesional de Python'`

La variable "titulo_curso" almacenará texto y mostrará este texto por consola si la variable se imprime.

Si deseamos que las comillas dobles sean parte de nuestra cadena de texto debemos crear nuestra variable String mediante comillas simples y por el contrario si deseamos que las comillas simples sean parte de nuestra cadena de texto entonces definimos nuestra variable con comillas dobles, por ejemplo:

`mensaje = '"Esto es un mensaje simple"'`
|- "Esto es un mensaje simple"


`mensaje = "'Esto es un mensaje simple'"`
|- 'Esto es un mensaje simple'

Si la cadena de texto es de múltiples líneas o es una cadena muy extensa se puede hacer uso de triple comillas simples o triple comillas dobles para definir el tipo de nuestra variable.

`mensaje = '''Esto
	Es un mensaje muy
	Extenso'''`

El tipo de dato "Int" es para almacenar valores numéricos, específicamente números enteros positivos o números enteros negativos.

Por ejemplo:

`numero_uno = 10`
`numero_uno = -10`

Cuando se desea trabajar con números reales (de tipo float) o también conocidos como números decimales se pueden almacenar de la siguiente manera:

`numero_dos = 3.1416`
`numero_dos = -3.1416`

Siempre que se trabaje con variables que contengas valores numéricos enteros o decimales podemos hacer uso de operadores aritméticos como la suma, resta, etc.

Por ejemplo:

`numero_dos = 10 + 20`

Nota: si quisieramos que una variable almacenará el resultado de una división con un resultado entero se puede hacer uso de la doble diagonal como se puede ver en el ejemplo.

`numero_dos = 10 // 3`

El tipo de dato boolean se caracteriza porque únicamente puede almacenar 2 valores ya sea verdadero o falso y estos se escriben en inglés y con la primer letra en mayúsculas.

`valor = True`
`valor = False` 



### Conclusión 

En Python no existen las constantes, pero la comunidad ha adoptado las variables con un nombre en mayúsculas como una variable constante.