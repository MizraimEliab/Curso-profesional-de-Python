# Clase 74 - Curso de Python - Atributos de instancia

## Notas de clase

### Introducción

Los atributos de instancia son aquellos atributos que le pertenecen a un objeto.

En Python nosotros podemos añadir de forma dinámica atributos a nuestro objeto, esto en tiempo de ejecución, para  esto internamente Python trabaja con un meta atributo  que tiene por nombre "__dict__" dentro de este atributo vamos a encontrar todos los atributos que tenga nuestro objeto.

### Atributos de instancia

Para que podamos ver el atributo podemos imprimir el meta atributo de nuestro objeto de la siguiente manera.

```
print(user1.__dict__)
```

Este atributo almacenará mediante un diccionario todos aquellos atributos que posea nuestro objeto.

El resultado será un diccionario vacío.

Cuando nosotros utilizamos un atributo para nuestro objeto Python realiza los siguientes pasos:

    1. Verifica si el atributo existe dentro del objeto.
    2. Verifica si el atributo existe dentro de la clase (Solamente funciona para lectura).
    3. Lanzar un error.

Estos 2 pasos siempre los usa Python y a pesar de que el objeto no tiene el atributo "username" Python retorna el atributo de clase para no obtener un error siempre y cuando el atributo exista de lo contario Python para al paso 3 y lanza un error.

Podemos confirmar que Python sigue esos 3 pasos para los atributos imprimiendo el id del  atributo desde el objeto y desde la clase.

```
print(id(user1.username))
print(id(Usuario.username))
```

### Conclusión 

En Python nosotros podemos añadir de forma dinámica en tiempo de ejecución atributos para nuestros objetos, estos atributos se van a almacenar en el meta atributo "__dict__".