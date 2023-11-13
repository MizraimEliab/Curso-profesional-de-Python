# Clase 16 - Curso de Python - Crear múltiples variables

## Notas de clase


### Introducción
Ya que sabemos como crear variables en Python podemos comenzar a crear y usar las variables que se necesiten para nuestros programa, sin embargo, hay una manera de declarar múltiples variables en una sola línea de código que nos permite tener un script más limpio y legible.


### Crear múltiples variables

A manera de ejemplo podemos tener el siguiente código, que si bien funciona muy bien es posible reducirlo.

`nombre = 'Alan'`
`apellido = 'Morales'`
`titulo = 'Sr.'`

`print(nombre)`
`print(apellido)`
`print(titulo)`

Para reducirlo se puede hacer uso de las comas en las variables y en los valores donde los valores se asignan en base a la posición de la variables.

`nombre, apellido, titulo = 'Alan', 'Morales', 'Sr.'`

Con esto si imprimimos las variables obtendremos el mismo resultado del ejemplo anterior.

Ya que en Python la legibilidad cuenta mucho si usamos una sola línea para crear muchas variables después pude generar un problema de legibilidad.

Como recomendación se deben crear variables de esta manera con un máximo de 4 variables siempre y cuando tengan el mismo contexto, es decir que se encuentren relacionadas.


### Conclusión 

El crear múltiples variables en la misma línea permite tener un código más limpio, sin embargo, hay que tener en cuenta que solamente es recomendable hacer esto con un máximo de 4 variables que estén relacionadas o tengan el mismo contexto para evitar que sea muy complicado leer el código en el futuro.