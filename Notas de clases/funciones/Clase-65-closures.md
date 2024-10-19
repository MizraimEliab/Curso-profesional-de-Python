# Clase 65 - Curso de Python - Closures

## Notas de clase

### Introducción
Un closure es una función que puede generar de forma dinámica a otra función y esta nueva función puede acceder a las variables locales aún cuando la primera haya finalizado.

Un concepto algo complejo que es más entendible con un ejemplo.

### Closures

Revisaremos el ejemplo de un closure.

```
def saludar(username):
    mensaje = f'Hola {username}' # Variable local

    def mostrar_mensaje(): # Anidada
        print(mensaje)
    return mostrar_mensaje

username = 'Alan'
respuesta = saludar(username)

respuesta()
```

En este ejemplo podemos visualizar una función principal que es "saludar" que tiene una variable local y a su vez cuenta con una función anidada que es "mostrar_mensaje", esta función anidada imprime la variable mensaje de la función principal y luego es retornada la función.

Finalmente se crear una variable "username" para tener un nombre de usuario y luego se guarda en una variable "respuesta" lo que retorne la función saludar pasando como argumento nuestra variable "username".

En este ejemplo vemos una pequeña diferencia y es que la función anidada (mostrar_mensaje) puede acceder a las variables de la función principal (saludar).

Esto es una excepción a la regla ya que las variable locales solo pueden ser utilizadas en el bloque que fueron creadas por lo tanto un closure es esto, esa excepción a esta regla.

La función principal (saludar) es un closure ya que retorna una función que puede acceder a las variables locales aún cuando la primera haya finalizado.

Podemos decir que la función anidada (mostrar_mensaje) de cierta forma tiene memoria ya que recuerda las variables locales que fueron creadas anteriormente.

Si modificaramos el valor de la variable "username" que tiene como valor "Alan" por cualquier otro valor seguiriamos saludando a "Alan".

### Conclusión 

Entonces un closure es una función que retorna otra función y a su vez esta nueva función puede acceder a las variables locales aún cuando la primera haya finalizado.

Esta nueva función tiene memoria de variables que fuera creadas en niveles superiores.