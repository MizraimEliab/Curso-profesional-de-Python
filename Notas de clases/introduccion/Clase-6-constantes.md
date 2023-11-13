# Clase 6 - Curso de Python - Constantes

## Notas de clase


### Introducción
Las contantes son variables que no permiten que se modifique su valor, en mucho lenguajes de programación incluso cuando una constante es declarada los compiladores marcan error cuando se ejecuta el script que intenta cambiar el valor de una constante, en Python las constantes no existen, el lenguaje trata a todas la variable como tal, sin embargo, la comunidad de desarrolladores por convención toma como constantes en Python aquellas variables cuyo nombre se encuentre escrito en su totalidad con mayúsculas.


### Variables
Para declarar una variable de solo lectura y posteriormente consultar su valor se puede realizar como el siguiente ejemplo:

`TITULO_CURSO = 'Curso profesional de Python'`

`print(TITULO_CURSO)`

El valor de esa variable puede ser modificado en tiempo de ejecución, sin embargo, por convención no debería ser escrito un nuevo valor en la variable ya que es tomada como una constantes.



### Conclusión 

En Python no existen las constantes, pero la comunidad ha adoptado las variables con un nombre en mayúsculas como una variable constante.