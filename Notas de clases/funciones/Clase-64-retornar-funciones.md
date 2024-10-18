# Clase 64 - Curso de Python - Retornar funciones

## Notas de clase

### Introducción
Como se mencionó en una lección pasada las funciones en Python son ciudadanos de primera clase esto quiere decir que funciones pueden retornar funciones.

### Retornar funciones

Vamos a revisar un ejemplo de como una función puede retornar otra función.

```
def saludar():

    def mostrar_mensaje():
        print('Hola nos encontramos de nuevo!')
    return mostrar_mensaje

respuesta = saludar()
print(respuesta)
```

Esto nos da como resultado una salida de que estamos retornando una función con su respectivo nombre y con esa salida se comprueba que nuestra función "saludar" esta retornando a nuestra función anidada "mostrar_mensaje".

Finalmente podemos comprobarlo imprimiendo el tipo de nuestra variable respuesta o bien mandando a llamar a la función a través de la variable respuesta.

```
def saludar():

    def mostrar_mensaje():
        print('Hola nos encontramos de nuevo!')
    return mostrar_mensaje

respuesta = saludar()
print(respuesta)
print(type(respuesta))

respuesta()
```

### Conclusión 

De esta manera es como podemos retornar funciones y poder llamarlas a través de nuevas variables que ocupemos y asignemos a ellas.