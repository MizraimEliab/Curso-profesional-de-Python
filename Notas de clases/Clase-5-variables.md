# Clase 5 - Curso de Python - Variables

## Notas de clase


### Introducción
En programación una variable es una dirección en memoria de la computadora donde seremos capaces de almacenar diferentes valores, una variable será representada mediante una etiqueta o mediante un nombre, comúnmente las variables modifican su valor en tiempo de ejecución, de ahí su nombre "variable".

Usualmente se asocia una variable a la analogía de la caja, donde la caja puede tener diferentes elementos dentro, sin embargo, para Python no es la correcta, en Python las variables se deben ver como etiquetas, esto para sacarle el máximo provecho al lenguaje.

Recuerda en Python las variables se ven como etiquetas.


### Variables
Ahora crearemos nuestras primeras variables.

Lo primero que debemos hacer es crear nuestro archivo (script que contendrá nuestras variables), entonces una vez creado pasamos a las siguientes consideraciones.

Las variables deben contener la siguiente estructura:

	- Nombre de la variable (Debe ser descriptivo que por si solo nos permita conocer que valores almacena).
	- Agregar el signo igual seguido del nombre de la variable
	- Finalmente después del signo de igual, agregar el valor de la variable

`nombre_variable = valor_variable`

Con esto ya esta definida una variable y puede ser utilizada n cantidad de veces que la necesitemos, esto es un ejemplo de una variable:

`curso: 'Curso profesional de Python'`

Ahora podemos hacer lectura de la variable y mostrar su valor por consola mediante la función print de la siguiente manera:

`print(curso)`

Esto al correr nuestro script debe regresar el mensaje por consola:

`Curso profesional de Python`

Al poder modificar el valor de una variable en tiempo real podemos hacerlo asignando un nuevo valor a la variable después del anterior como se muestra en el siguiente ejemplo:

`curso: 'Curso profesional de Python'`
`curso: 'Curso Python'`
`print(curso)`

Ahora si volvemos a ejecuta nuestro programa la salida sería:

`Curso Python`

Ya que es nuestro último valor asignado a la variable ya que la ejecución de un programa es de manera descendente, es decir del comienzo al final del script.

IMPORTANTE: Siempre dale nombres descriptivos a tus variables y evita nombres como "a", "x", etc. Esto puede dificultar la lectura del código en un futuro de ahí la importancia de darle nombres descriptivos a las variables.

Por ejemplo para el ejemplo anterior podemos agregar un nombre más descriptivo:

`titulo_curso =  'Curso profesional de Python'`

Ya que es más descriptivo el nombre de nuestra variable al tener más de una letra podemos hacer uso de la nomenclatura de snake case que indica que separáremos las palabras mediante un guion bajo y todas las palabras en minúsculas como en el ejemplo anterior.

Lo anterior es un buena práctica.


### Conclusión 

Para generar buenas prácticas es importante que el nombre de nuestra variable sea auto descriptivo y que permita conocer de primera mano el valor que contiene sin la necesidad de conocer o buscar la información en la documentación del software.

IMPORTANTE: Python maneja palabras reservadas que no pueden usarse ya que entraríamos en conflicto con el lenguaje.