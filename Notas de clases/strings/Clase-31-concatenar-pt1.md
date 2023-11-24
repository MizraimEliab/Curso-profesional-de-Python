# Clase 31 - Curso de Python - Concatenar pt 1

## Notas de clase


### Introducción
Los string en Python son inmutables, esto quiere decir que nosotros no podremos modificarlo en tiempo de ejecución y así se quedará por el resto del programa, si deseamos modificar los string no podremos, pero lo que si podemos hacer es generar nuevos strings a partir de otros strings. 


### Concatenar pt 1

Vamos a generar un nuevo string a partir de otros strings para ello imaginemos 2 variables, una con un nombre y otra con un apellido.

`nombre = 'Alan Isaac'`
`apellido = 'Turing'`

Si quisiéramos generar el nombre completo en una sola variable se puede hacer uso del operador "+" para unir las variables en otra y de esta manera generar un nuevo string.

`nombre_completo = nombre + ' ' + apellido`
`print(nombre_completo)`

Con el operador "+" podemos unir n cantidad de strings y a esto se le conoce como concatenar strings.

Otra manera de concatenar es haciendo uso de "%s" donde primero creamos un string base con el cual trabajaremos y luego después indicamos que strings deben sustituir esos "%s" para hacer nuestro nuevo string.

`nombre_completo = 'Sr. %s %s.' % (nombre, apellido)`
`print(nombre_completo)`

Como se puede observar para sustituir los "%s" se debe indicar después de las comillas simples el signo de porcentaje y dentro de parentesis las variables a colocar en nuestro nuevo string separadas por coma. Al igual que la primera forma de concatenar podemos usar n cantidad de valores para construir nuestro string de esta manera.

### Conclusión 

En base a estas 2 formas podemos concatenar strings y generar nuevas cadenas de texto a partir de otras, el uso depende de cada desarrollador y el contexto general del software que se este desarrollando.