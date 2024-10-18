# Clase 52 - Curso de Python - Argumentos

## Notas de clase

### Introducción
Como se ha mencionado en lecciones anteriores existen valores de entrada para que nuestra función pueda ejecutar determinada lógica y acciones.

### Argumentos

Los argumentos de una función son variables que se indican dentro de los parentesis de la función como los valores de entrada que serán almacenados en estas variables.

Estas variables también se conocen como parámetros de la función.

Para revisar la sintaxis se pude usar la función suma vista en una lección pasada, que en términos generales solamente editamos esa función para hacerla más abstracta para el uso de parámetros.

Los parametros pueden ser n cantidad y deben ir separados por coma dentro de los paréntesis de la función.


```
def suma(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    print(resultado)

numero_uno = int(input('Ingresa el primer número entero:'))
numero_dos = int(input('Ingresa el segundo número entero:'))
suma(numero_uno, numero_dos)

```

Cuando se invoca la función se le deben pasar los parámetros en el orden como se declararon en la función, es decir, con respecto a su posición, si no se pasan los parámetros Python nos marcará error.



### Conclusión 

A la función no le interesa de donde lleguen los valores de entrada, es decir, sus parámetros solamente no marcará error siempre y cuando tenga los valores cuando la función sea invocada, también es importante comentar que el nombre de las variables de parámetros en la función puede no ser el mismo al de las variables que se pasan en la invocación y no hay problema ya que los parámetros solamente existen en el bloque de código de la función.