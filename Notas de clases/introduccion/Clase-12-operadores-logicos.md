# Clase 12 - Curso de Python - Operadores lógicos

## Notas de clase


### Introducción
En Python contamos con 3 operadores lógicos, estos son:
	- and
	- or
	- not
Y a diferencia de los operadores relacionales que nos permiten comparar tipos numéricos ya sean enteros o flotantes, los operadores lógicos nos permiten comparar tipos boolean, este tipo de operadores obtendremos como resultado un valor boolean ya sea verdadero o falso. 


### Operadores lógicos

Dentro de Python se usan las palabras tal cual para estos operadores, si has trabajado con otros lenguajes de programación seguramente sabrás que por ejemplo para hacer uso del and se utiliza doble && en este caso para Python no, se escribe tal cual la palabra "and".

El operador lógico "and" nos permite comparar valores boolean donde todas las comparaciones deber ser verdaderas para que el resultado final sea verdadero, si una sola comparación es falsa entonces el resultado final será falso.

Por ejemplo:

`resultado_final = True and True`
`print(resultado_final)`
`True`

Es importante mencionar que podemos usar los operadores lógicos que deseemos en la línea de código.

También es posible combinar en una sola línea de código operadores lógicos y relacionales, por ejemplo:

`resultado_final = True and True and 10 > 20`

El operador lógico "or" por lo menos una de las comparaciones debe ser verdadera para que el resultado final sea verdadero. En otros lenguajes de programación se usan los pipes para indicar el operador, en Python no es necesario y solo basta con escribir la palabra "or".

`resultado_final = True or True or False`
`print(resultado_final)`
`True`

En el operador "or" si todas las comparaciones son falsas el resultado final será falso.

Si hacemos uso de paréntesis () podemos combinar los operadores lógicos, lo cual permite realizar comparaciones más complejas.

`resultado_final = True and (False or 5 > 10 )`

En este caso Python siempre resolverá primero lo que se encuentra en los paréntesis y posteriormente lo de fuera.

`False`

Finalmente el operador lógico "not" permite negar un valor boolean, convierte "True" a "False" y viceversa.

`resultado_final = not True`
`print(resultado_final)`
`False`

### Conclusión 

Los operadores lógicos nos permiten trabajar con valores boolean y poder hacer comparaciones complejas incluso combinando con operadores relacionales.