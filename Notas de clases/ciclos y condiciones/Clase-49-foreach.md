# Clase 49 - Curso de Python - Foreach

## Notas de clase

### Introducción
El ciclo "for" en Python es un ciclo "Foreach" y es la forma de iterar los elementos dentro de una colección, dentro de un objeto iterable, que en este caso puede ser un string, una tupla, una lista o un diccionario.

### Foreach

Para realizar la iteración con un ciclo "for" basta con crear una variable que será nuestra variable que recorra la estructura de datos y  siempre se recomienda nombrarla con el mismo nombre de la colección a iterar solamente que en singular.


```
usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4']

for usuario in usuarios:
    print(usuario)

```


En este ejemplo mostrado en el primer recorrido nuestra variable usuario tomará el string "usuario1" de la lista de usuarios, en su segundo recorrido tomará el string "usuario2" y así sucesivamente, es importante mencionar que la variable usuario solo estará disponible dentro del bloque "for".


### Conclusión 

El ciclo "for" nos ayudará mucho a recorrer los datos de las diferentes estrcuturas de datos que tenemos en Python haciéndolo muy útil para acciones dentro de una gran variedad de datos.

Al no usar una condición en la estrcutura original del ciclo "for" no es posible usar la sentencia "else".