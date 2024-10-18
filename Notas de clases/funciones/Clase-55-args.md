# Clase 55 - Curso de Python - Args

## Notas de clase

### Introducción
En Python podemos tener funciones que puedan recibir n cantidad de argumentos, los que se requieran para esta función.

Un ejemplo de esta funciones ya lo usamos con la función "print()" que le puedes pasar n cantidad de argumentos para que estos sean mostrados por consola. La función "print()" no se encuentra limitada a recibir una cantidad de argumentos.

Esta funciones son muy útiles y podemos aprovecharlas para cuando no se sepa el número de argumentos que serán recibidos por la función.

### Args

Para revisar como podemos hacer uso de estas funciones vamos a crear una función de ejemplo que calcule el promedio de una lista de números enteros.

```
def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio([10, 10, 5, 7, 10])
print(resultado)
```

Este ejemplo anterior funciona, pero que pasa si le quitamos los corchetes de las lista y dejamos los valores, esto nos daría un error de argumentos, ya que la función espera 1 solo argumento y se le están pasando 5 que vienen siendo los números del listado.

Para poder usar nuestro argumento y los valores que se le pasan a la función deberemos agregar un asterisco como prefijo y sin espacio de nuestro parámetro y esto Python lo entenderá como que todos los valores que le pasemos a la función los almacenará en una tupla para posteriormente ser usada dentro de la función, con esto nuestro problema de argumentos esperados se resuelve y la función vuelve a funcionar correctamente.

```
def promedio(*args):
    print(args)
    print(type(args))
    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)
```

Por convención de la comunidad de Python todos los parámetros que llevan asteriscos se nombran como "*args" 

### Conclusión 

Las funciones con parámetros con asterisco nos ayudan a almacenar n cantidad de argumentos en una tupla para posteriormente usar toda esa información dentro de nuestra función, esto es muy útil cuando varia la cantidad de argumentos que se pueden mandar a la función.