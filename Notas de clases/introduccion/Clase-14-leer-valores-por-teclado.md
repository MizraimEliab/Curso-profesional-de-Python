# Clase 14 - Curso de Python - Leer valores por teclado

## Notas de clase


### Introducción
Hasta el momento hemos colocado los valores de las variables en el mismo script, sin embargo, habrá ocasiones donde nuestro programa requiera de valores de entrada para trabajar.

Estos valores de entrada pueden venir de diferentes lugares, pueden venir de una base de datos, una API o directamente de un usuario vía teclado.


### Leer valores por teclado

Centrado en capturar un valor de entrada a nuestro programa hacemos uso de la función "input" para agregarle un mensaje y usar el valor.

Para este ejemplo tomaremos en cuenta que se va a guardar la información de una persona.

A la función input podemos pasarle opcionalmente un mensaje, lo cual es recomendable para darle mayor contexto al usuario sobre que tipo de dato debe escribir.

`input('Ingresa tu nombre completo: ')`

La función "input" se encarga de pausar la ejecución de nuestro programa y esperar un valor y va a regresar todo lo que el usuario escribió hasta que se presiono entrar en el teclado.

El valor que regresa la función lo podemos almacenar en una variable y posteriormente manipular ese valor como se desee.

`nombre_completo = input('Ingresa tu nombre completo: ')`
`print(nombre_completo)`

Es importante mencionar que la función "input" siempre va a retornar un tipo de dato string, es decir, una cadena de caracteres. Esto se debe tomar en cuenta ya que si se quieren trabajar con otros tipos de datos como enteros o reales se deben transformar esos valores a partir de los strings de la función "input".


### Conclusión 

La función "input" que nos sirve para leer valores de entrada por teclado en Python recibe como argumento  opcional un mensaje, el cual puede ser empleado para dar contexto del valor a ingresar.