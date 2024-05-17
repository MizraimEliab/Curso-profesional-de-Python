# Clase 42 - Curso de Python - Tipo None

## Notas de clase

### Introducción
En adición a los tipos de datos que se han revisado Python cuenta con un tipo de dato básico llamado "None" que como su nombre lo indica es un tipo de dato para un valor vacío.

Siempre se usará "None" para representar la ausencia de un valor.

Se pueden crear variables de tipo "None" cuando aún no sabemos que tipo de valor obtendrá la variables a lo largo de la ejecución del programa.  

### Tipo None

Un escenario para este tipo de dato en Python es cuando queremos recibir información de una API, al momento nos sabemos en que tipo de dato o estructura llegará la respuesta y para ello definimos una variable que de momento será tipo "None".

`resultado = None`

Como se puede ver declarar una variable de tipo "None" es muy sencillo y este tipo de dato puede ser el equivalente al valor nulo en otros lenguajes de programación.


### Conclusión 

Si se imprime el tipo de una variable "None" la consola nos mostrará que es una variable de tipo "NoneType" que significa que no tiene tipo.

Con "None" en Python representamos la ausencia de un valor, sin embargo, Python al ser un lenguaje de tipado dinámico la variable que inicia en "None" eventualmente pude cambiar el valor durante la ejecución del programa.