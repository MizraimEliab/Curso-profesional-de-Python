# Clase 44 - Curso de Python - Condiciones

## Notas de clase

### Introducción

Ahora que ya se conocen las estrcuturas de datos se revisarán las estructuras de código, en diferentes momentos tendremos la necesidad de ejecutar ciertos bloques de código cuando se cumplan ciertos criterios, o bien que es lo mismo condicionar nuestro programa. 

### Condiciones

Para condicionar en Python haremos uso de la palabra reservada "if"  veamos un ejemplo.

```
resultado = 10
if resultado > 10:
    print('La variable cumple con la condición.')
```

Como podemos observar en el ejemplo estamos condicionando un mensaje y es importante notar la estructura de nuestra condición que se compone por la palabra reservada "if" seguida de una expresión o valor boolean luego se indican ":" para dar apertura al bloque y por convención se usa el identado que utiliza 4 espacios.

Algo importante a destacar es que en la expresión hacemos uso de un operador relacional que para este ejemplo es el conocido mayor que ">" para comparar nuestra variable con un valor. 

El bloque dentro de nuestra condición se va a ejecutar siempre y cuando el valor sea verdadero.

Si se ejecuta el programa anterior la consola no mostrará el mensaje pero tampoco marcará algún tipo de error, esto se debe a que el resultado de la expresión de nuestra condicional nos regresa un valor falso y por lo tanto no nos muestra el mensaje por consola.

Si cambiáramos el valor de la variable resultado por un valor mayor a 10 entonces la condición se cumpliría y nos mostraría nuestra mensaje por consola al ejecutar el programa.

```
resultado = 11
if resultado > 10:
    print('La variable cumple con la condición.')
```

Además de hacer uso de operadores relacionas podemos hacer uso de operadores lógicos para hacer una expresión más compleja.

```
resultado = 11
if resultado > 10 and resultado < 20:
    print('La variable cumple con la condición.')
```

Esta condición indica que si el valor que contiene nuestra variable resultado se encuentra dentro del rango de 10 y 20 imprimirá por consola el mensaje, es decir la expresión debe resultar verdadera.

Si nosotros deseamos agregar un mensaje u otra opción cuando la empresión de nuestra condición resulte falsa podemos hacer uso de la palabra reservada "else" y luego agregar 2 puntos para apertura del bloque de código a ejecutar.

```
resultado = 11
if resultado > 10 and resultado < 20:
    print('La variable cumple con la condición.')
else:
    print('La variable no cumple con la condición..')
```

### Conclusión 

Haciendo uso de la palabra reservada "if" y "else" podemos condicionar bloques de código haciendo uso del resultado de alguna expresión que nos retorne un valor boolean y la condición se cumplirá siempre y cuando el valor boolean sea verdadero.

Es importante tener en cuenta que para crear el bloque debemos agregar 2 punto e identar con 45 espacios por convención.