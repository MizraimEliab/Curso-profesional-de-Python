# Clase 51 - Curso de Python - Funciones

## Notas de clase

### Introducción
Las funciones son bloques de código que realizan una operación y devuelven un resultado ya sea explícito o implícito.

En Python para definir una función se hace uso de la palabra reservada "def" y seguido de la palabra reservada se indica el nombre que tendrá la función, luego los parentesis donde irán o no los parámetros de la función y finalmente los doble puntos de apertura de bloque de código. 

Los parámetros son variables de entrada que funcionarán dentro de nuestra función para ser procesadas o leídas dentro de la función.  

### Funciones

Se muestra un ejemplo de una función que sume 2 números enteros, el funcionamiento será el siguiente: la función pedirá 2 números enteros por teclado al usuario y luego se mostrará la suma de los 2 números ingresados.


```
def suma():
    numero_uno = int(input('Ingresa el primer número entero:'))
    numero_dos = int(input('Ingresa el segundo número entero:'))

    resultado = numero_uno + numero_dos

    print(resultado)

suma()

```

Como se puede observar es importante mandar a llamar o invocar a la función haciendo uso de su nombre y sus parámetros, en este caso como no cuenta con parámetros simplemente se queda con los parentesis.

Es importante tener en cuenta que al igual que las variables debemos seguir la estrcutura "snake_case" para nombrar a las funciones, es decir usar guion bajo para conectar varias palabras y todo escrito en minúsculas .

Algo importante como se muestra en el ejemplo es que dentro de una función se pueden llamar otras funciones, como por ejemplo la función "int", "input" y "print".

También es importante mencionar que las funciones se pueden llamar n cantidad de veces.



### Conclusión 

Así podemos crear nuestra funciones en Python y están diseñadas para realizar una tarea particular. 