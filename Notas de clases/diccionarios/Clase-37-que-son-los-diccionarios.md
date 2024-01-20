# Clase 37 - Curso de Python - ¿Qué son los diccionarios?

## Notas de clase

### Introducción
Un aspecto interesante en Python es que nosotros podemos alinearlos o justificarlos mediante el uso de métodos.

### ¿Qué son los diccionarios?

Para alinear o justificar el texto en Python podemos hacer uso de 3 métodos lo cual se traduce en que tenemos 3 maneras de lograr justificar el texto.

Los 3 métodos son los siguientes:
	- ljust -> Alinea el texto a la izquierda
	- rjust -> Alinea el texto a la derecha
	- center -> Alinea el texto al centro

Es importante mencionar que los 3 métodos no modifican al string original, si no que, a partir del string se genera uno nuevo ya que los string en Python son objetos inmutables.

Vamos a comenzar a ver el ejemplo de alineación a la izquierda.

`mensaje = mensaje.ljust(20)`
`print(mensaje, '.')`

Como se puede observar al método se le pasa un argumento que indica la cantidad de espacios a agregar para justificar el texto.

El argumento aplica igual para el método de alineación a la derecha y para alineación al centro.

`mensaje = mensaje.rjust(20)`
`mensaje = mensaje.center(20)`


### Conclusión 

Siempre que se requiera alinear un string para manejo de datos o simplemente acomodo de la información se puede hacer uso de los 3 métodos de alineación que nos proporciona Python.