# Clase 35 - Curso de Python - Validar sub strings

## Notas de clase


### Introducción
Después de haber revisado las formas en Python de poder generar nuevos strings a partir de otros strings hemos visto los resultados mediante la consola con la función "print()", sin embargo, siempre le pasamos una variable como argumento, si bien es cierto esto no esta mal es importante saber que podemos omitir la variable y pasarle solo los valores a la función "print()".

### Validar sub strings

Si recordamos la función "print()" nos permite imprimir por consola valores, pero es importante saber que no solamente podemos imprimir un solo valor ya que la función nos permite imprimir múltiples valores.

`nombre = 'Alan Isaac'`
`apellido = 'Turing'`
`print(nombre, apellido, 'Arch')`

Como se puede observar los valores de la variables y el valor que se indicó están separados por coma dentro de una sola línea que usa la función "print()".

Lo interesante es que imprimirá los valores y los separará usando un espacio.

La función "print()" se encargará de imprimir por consola todos los valores que le pasemos a la función como argumento, ya sean string, enteros, flotantes, etc.

`print(nombre, apellido, 'Arch', True)`

Ahora que conocemos que por defecto la función "print()" separa los valores por un espacio, ¿Qué pasa si queremos que separe los valores por otro caracter?, bueno la respuesta a la pregunta es que podemos hacerlo apoyándonos del parámetro "sep" y el caracter a utilizar para separar los valores.

`print(nombre, apellido, 'Arch', sep='-')`

El parámetro "sep" se recomienda utilizarlo al final dentro de la función "print()" después de nuestros valores.

### Conclusión 

Es importante mencionar que la función "print()" únicamente va a imprimir en consola, en ningún momento va a generar un nuevo string.