# Clase 23 - Curso de Python - Matrices

## Notas de clase


### Introducción
En Python utilizando listas seremos capaces de trabajar con matrices de una manera muy simple, ya que como se menciono anteriormente con las listas podemos almacenar otros tipos de datos, incluidas otras listas con lo cual seremos capaces de crear matrices de n dimensiones.


### Matrices

Podemos por ejemplo crear una matriz de 2 dimensiones mediante el uso de 2 variables, también se le conoce a esta matriz como bidimensional.

`columna_a = [10, 20]`
`columna_b = [30, 40]`
`matriz = [columna_a, columna_b] # 2 x 2`
`print(matriz)`

Con este ejemplo ya contamos con una matriz de 2 dimensiones debido a que tenemos 2 filas y 2 columnas y en consola esto se refleja como una lista que almacena otras listas.

Al ser una matriz de 2 dimensiones y guardar un lista dentro de otra para el acceso a los índices es ingresar mediante x, y respetando la regla matemática y accediendo a los elementos como se había visto anteriormente.

`print(matriz[0][0])` 
`10`

Por su puesto se pueden crear matrices de más dimensiones y más complejas como lo queramos.


### Conclusión 

De esta manera a través de listas que almacenen otras listas seremos capaces de crear matrices en Python.