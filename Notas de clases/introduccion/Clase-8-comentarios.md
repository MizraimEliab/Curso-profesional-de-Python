# Clase 8 - Curso de Python - Comentarios

## Notas de clase


### Introducción
Cuando nos encontramos en la fase de desarrollo comúnmente se requiere realizar anotaciones para tener observaciones sobre el código que estemos desarrollando o bien notas importantes para describir alguna pieza de código.

Estas notas las conoceremos como comentarios y para realizarlos tenemos 2 formas de hacerlo en Python.


### Comentarios
La primera manera de hacer un comentario en Python es mediante el uso del signo numeral o también conocido como el signo del gato #, posteriormente se indica el comentario sobre la misma línea donde se escribió el numeral como se puede ver en el siguiente ejemplo:

`# Esta línea se encuentra comentada`

Es importante mencionar que las líneas comentadas no serán tomadas en cuenta al momento de ejecutar el programa. La validación de un comentario se puede realizar quitando el signo del numeral y ejecutando el script, con esto, Python marcará un error de sintaxis al no reconocer nuestra frase. 

El signo numeral # únicamente nos permite comentar una sola línea de código es la primer forma de realizar un comentario, pero ¿Qué pasa cuando se quieren comentar más líneas de código?.


La segunda manera de hacer comentarios en Python es mediante el uso de triple comillas dobles, es decir, indicando tres veces las comillas dobles como apertura del comentario y otra tres veces comillas dobles como cierre, esta manera se diferencia de la primera ya que esta es empleada para comentar múltiples líneas de código en lugar de una sola línea.

Aquí el ejemplo:

`"""
Este es un comentario
que posee saltos
de línea.
""" `



### Conclusión 

Tenemos 2 formas de comentar en Python que nos ayudan a dejar indicaciones, notas, descripciones u observaciones del código, cada forma de comentar te permite dejar esa nota sin que estos comentarios afecten a la ejecución del programa ya que Python los toma como comentarios.