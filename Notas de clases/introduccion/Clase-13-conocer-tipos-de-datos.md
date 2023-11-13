# Clase 13 - Curso de Python - Conocer tipos de datos

## Notas de clase


### Introducción
Si por alguna razón quisiéramos saber que tipo de dato esta almacenando una variable, esto es posible gracias a la función "type".


### Conocer tipos de datos
Mediante la función "type" de Python podemos conocer el tipo de dato que una variable almacena y de esta manera saber el tipo.

`valor = "Hello"`
`tipo = type(valor)`
`print(tipo)`
`<class  'bool'>`

Esto es funcional, sin embargo, lo más conveniente es que nosotros imprimamos directamente la función para conocer el tipo y ahorrar una variable.

`print(type(valor))`


### Conclusión 

Siempre que se requiera conocer el tipo de dato que almacena una variable podemos hacer uso de la función "type" y en base a su resultado operar mejor con la variable examinada.