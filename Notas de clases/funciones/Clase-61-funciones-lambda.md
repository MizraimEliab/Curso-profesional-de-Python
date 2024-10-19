# Clase 61 - Curso de Python - Funciones lambda

## Notas de clase

### Introducción
Ahora que conocemos que en Python las funciones son ciudadanos de primera clase ahora revisaremos las funciones lambda o también conocidas como funciones anónimas que son funciones expresadas en una sola línea de código además de no poseer un nombre debido a que estas funciones realizan acciones muy pequeñas. 

### Funciones lambda

Para crear una función lambda de ejemplo vamos a hacer una función que convierta los grados centígrados en grados Fahrenheit, veamos el ejemplo.

```
funcion_grados = lambda grados : grados * 1.8 + 32

```

Como se observa en el ejemplo se inicializa una variable y se asigna a una función lambda con el uso de la palabra reservada "lambda" seguido del parámetro de la función (En caso de requerir más parámetros se deben separar por comas después de la palabra reservada lambda) luego hacemos uso de los 2 puntos y finalmente seguido de los 2 puntos el cuerpo de la función donde se obtendrá un resultado y la función lambda lo retorna por default ya que nos es necesario usar la palabra reservada "return" para retornar el valor de la función.

Para mandar a llamar a nuestra función es simple ya que la hemos almacenado en una variable deberemos imprimir la variable con los parámetros necesarios para la función.

```
print(funcion_grados(16))
```

A pesar de que las funciones lambda son sencillas las podemos complicar agregando por ejemplo más parámetros, veamos los siguientes ejemplos.

```
sin_parametros = lambda : True
parametros_default = lambda a1=10, a2=20, a3=30 : a1 + a2 + a3
asterisco = lambda *args, **kwargs : len(args) + len(kwargs)
```

Es importante mencionar que siempre que creemos una función lambda debe llevar forzosamente un cuerpo, por lo menos debe haber una expresión sencilla que se deba ejecutar  por muy simple que esta expresión sea.


### Conclusión 

La funciones lambda o funciones anónimas nos ayudan a ejecutar piezas de código simples en una sola línea manteniendo un código limpio usando estas funciones para expresiones comunes dentro de nuestro código, además las funciones lambda pueden usar la misma estructura de parámetros que cualquier función en Python.