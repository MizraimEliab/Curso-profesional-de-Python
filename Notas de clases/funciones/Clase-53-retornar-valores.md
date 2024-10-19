# Clase 53 - Curso de Python - Retornar valores

## Notas de clase

### Introducción
El retorno de valores de una función es cuando necesitamos que la función nos devuelva un resultado que posteriormente podemos mostrar al usuario, guardarlo en una base de datos o mandar ese dato a otra función.

### Retornar valores

Para retornar un valor de una función se usa la palabra reservada "return" y posteriormente el valor a devolver, en este caso una variable o un dato.

Dicho resultado se puede almacenar en una nueva variable.

Veamos como queda la función suma devolviendo solamente el valor de la suma de 2 variables obtenidas por entrada de usuario por consola.


```
def suma(numero_uno, numero_dos):
    return numero_uno + numero_dos

numero_uno = int(input('Ingresa el primer número entero:'))
numero_dos = int(input('Ingresa el segundo número entero:'))
resultado = suma(numero_uno, numero_dos)
print("El resultado de la suma es: ", resultado)

```

En Python podemos hacer que una función retorne múltiples valores solamente mediante el uso de coma y en ese sentido las variables pueden almacenar dichos valores con respecto a la posición del retorno de valores de la función, o si solamente usamos una variable Python por defecto genera una tupla con los valores que retorna la función.

```
def suma(numero_uno, numero_dos):
    return numero_uno + numero_dos, 'Función ejecutada correctamente'

numero_uno = int(input('Ingresa el primer número entero:'))
numero_dos = int(input('Ingresa el segundo número entero:'))

resultado, mensaje = suma(numero_uno, numero_dos)
print("El resultado de la suma es: ", resultado)
print("El mensaje es: ", mensaje)
```

### Conclusión 

En Python podemos retornar diferentes valores y de diferente tipo de dato de cada función que tengamos escrita, por defecto Python va a generar una tupla con todos los valores que retorne una función.

Se aconseja no retornar muchos valores, como recomendación retornar un máximo de 3 valores por cada función.