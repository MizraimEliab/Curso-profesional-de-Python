# Clase 27 - Curso de Python - Listas y tuplas

## Notas de clase


### Introducción
Sabemos ya que al definir una variable con valores entre corchetes es para una lista y una variable definida con valores entre paréntesis es para una tupla, ambas estructuras de datos cuentan con sus ventajas y desventajas y habrá ocasiones donde se usen las tuplas o las listas dependiendo de las necesidades particulares.


### Listas y tuplas


Cuando no conocemos el número de elementos que se van a guardar e incluso estos valores una vez guardados se van a modificar después haremos uso de la listas y si por el contario ya conocemos cuantos valores se van a almacenar y además estos valores nunca van a cambiar entonces haremos uso de tuplas.

Pero que pasa si mientras en tiempo de ejecución debemos generar listas a partir de tuplas o viceversa debemos generar tuplas a partir de listas, para ello podemos hacer uso de las funciones lista o tupla.

`cursos = ['Python', 'Flask', 'Django']`
`niveles = ('Basico', 'Intermedio', 'Avanzado')`

Generar tupla a partir de una lista.

Para generar una tabla a partir de una lista podemos hacer uso de la función "tuple()" para hacer dicha acción, solo basta con indicar como argumento a la función nuestra lista.

`cursos_tupla = tuple(cursos)`
`print(cursos_tupla)`

Generar lista a partir de una tupla.

Si queremos generar una lista a partir de una tupla podemos hacerlo con la función "list()" donde como argumento de la función le pasaremos la tupla de la cual partiremos para generar nuestra lista.

`niveles_lista = list(niveles)`
`print(niveles_lista)`


### Conclusión 

Mediante el uso dela función "list()" y "tuple()" seremos capaces de crear listas a partir de tuplas y viceversa y generar nuevas estructuras con las cuales podemos trabajar en tiempo de ejecución.