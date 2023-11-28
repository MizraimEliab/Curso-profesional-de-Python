# Clase 32 - Curso de Python - Concatenar pt 2

## Notas de clase


### Introducción
Existen otras maneras de generar nuevos strings a partir de strings ya definidos en nuestro programa, una manera muy útil es mediante el método "format()".


### Concatenar pt 2

Esta manera es parecida a la de uso del signo %s ya que requerimos de colocación de ordenes con la diferencia que no existe un signo separador, si no que, se hace uso del método "format()" y como argumentos se pasan los strings a concatenar.

`nombre_completo = 'Mr. {} {}.'.format(nombre, apellido)`
`print(nombre_completo)`

Como se puede observar además del uso del método "format()" en lugar del signo %s se hace uso de llaves "{}" para poder dejar el espacio que ocupará el string dentro de la concatenación con respecto a su posición.

Finalmente podemos asignar nombres a las llaves o placeholders en nuestra expresión, el único cambio que se haría es indicar esos nombres en los argumentos de nuestra función "format()".

`nombre_completo = 'Mr. {name} {last_name}.'.format(name=nombre, last_name=apellido)`
`print(nombre_completo)`

Lo interesante es que podemos modificar el orden de los signos o placeholders del string base y no del string de la función "format()", es decir al nombrar a los placeholders no se van a asignar respecto a la posición, si no que lo harán respecto a los nombres.



### Conclusión 

Con el método "format()" seremos capaces de generar un nuevo string a partir de diferentes strings y un string base y este será el que use el método "format()".