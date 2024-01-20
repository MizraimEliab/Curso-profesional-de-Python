# Clase 33 - Curso de Python - FString

## Notas de clase


### Introducción
Los Fstrings nos permiten generar nuevos strings a partir de otros utilizando interpolación.

### FString

Para crear un Fstring debemos tener un string base y justo antes del string base debemos indicar el caracter "f" para decirle a Python que nuestro string será un Fstring y dentro del string seremos capaces de usar interpolación, esto se puede lograr usando llaves dentro del string.

`nombre_completo = f'Mr. {nombre} {apellido}.'`
`print(nombre_completo)`

También dentro de las llaves podemos solamente indicar el valor string sin uso de variables.

`nombre_completo = f'Mr. {nombre} {apellido} {'Arch'}.'`


### Conclusión 

Se puede observar de una manera muy legible como se puede generar un nuevo string a partir de otros haciendo uso de la estructura Fstring de Python y podemos hacer uso de cualquier tipo de datos e incluso expresiones que al final del día se mostrará como string.

La legibilidad en el código es muy importante y mediante los Fstring tendremos una manera muy simple de leer nuestro string.