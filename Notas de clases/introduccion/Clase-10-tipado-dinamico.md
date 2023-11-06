# Clase 10 - Curso de Python - Tipado dinámico

## Notas de clase


### Introducción
Python es un lenguaje que usa tipado dinámico que en términos prácticos se traduce que una variable puede tener diferentes tipos de datos en diferentes momentos si esta se reasigna, es decir que una variable a lo largo de la ejecución de un programa puede contar con diferentes tipos de datos. 


### Tipado dinámico
Para entender el tipado dinámico de Python es importante revisar el siguiente ejemplo.

`valor = "Alan"`
`valor = 2`
`valor = 3.1`
`valor = True`

`print(valor)`

¿Qué valor se va a imprimir cuando se ejecute este script?

La respuesta a la pregunta anterior es el valor de "True" ya que cuando se ejecuta el script la variable va tomando cada valor con su respectivo tipo de dato hasta llegar al final que es el valor "True" de tipo boolean.


### Conclusión 

El tipado dinámico es muy útil durante el desarrollo, sin embargo, el no seguir un estándar de codificación y no nombrar de forma correcta a nuestras variables y hacer que estas almacenen tipos de datos de forma indiscriminada puede resultar en un código difícil de leer y comprender.

Por ello la recomendación es almacenar un tipo de dato por variable siguiendo una convención.