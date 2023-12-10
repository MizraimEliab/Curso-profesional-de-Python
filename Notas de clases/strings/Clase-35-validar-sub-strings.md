# Clase 35 - Curso de Python - Validar sub strings

## Notas de clase


### Introducción
Ahora se revisará la manera de buscar strings dentro de otros strings y para ello existen diferentes formas de hacerlo.

### Validar sub strings

Una manera de hacer la busqueda es mediante el uso del método "count()" que recibe como parámetro la coincidencia en string que vamos a buscar a partir de un string base, el método nos retorna la cantidad de veces que se encontro la coincidencia del string que pasamos como argumento en nuestro string base.

`titulo_curso = 'Curso profesional de Python'`
`contador = titulo_curso.count('Python')`
`print(contador)`
`1`

Con base al ejemplo se puede observar que existe nuestro string que buscabamos 1 sola vez en nuestro string base.

Con este método podemos buscar mediante una palabra o frase, y también podemos buscar por caracteres.

Si buscamos con el método "count()" un string que no existe en el string base simplemente nos retornara el valor cero.

Otra manera de buscar si un string existe dentro de otro es mediante el uso de la palabra reservada "in".

`print('Python' in titulo_curso)`
`True`

Como se puede ver la palabra reservada "in" nos regresa un boolean dependiendo si el string a buscar se encuentra o no en un string base.

Si la palabra "Python" la escribiéramos en minúscula "python" con la palabra reservada "in" nos regresaría un False ya que a Python si le importan el uso de mayúsculas y minúsculas.

Para obtener un verdadero podemos estandarizar el string base haciendo que todas las letras se pongan en minúscula con "lower()" o en mayúscula con "upper()".

También es importante que es posible negar con la palabra reservada "not".

`print('alan' not in titulo_curso.lower())`

Existen otros métodos para conocer si nuestro string base comienza o termina por un string en especial.

Esos métodos son "startswith()" y "endswith()" y ambos reciben como argumento el string a buscar como coincidencia basándose en otro string y ambos retornan un valor boolean.

`print(titulo_curso.startswith('Curso'))`
`print(titulo_curso.startswith('curso'))`
`print(titulo_curso.endswith('Python'))`
`print(titulo_curso.endswith('python'))`


### Conclusión 

Como podemos notar existen diferentes métodos con los cuales podemos ir buscando strings dentro de otros strings para hacer diferentes validaciones que nos pueden ayudar a la hora de hacer nuestros desarrollos.