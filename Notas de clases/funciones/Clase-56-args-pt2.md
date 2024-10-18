# Clase 56 - Curso de Python - Args pt2

## Notas de clase

### Introducción

Algo importante a tener en cuenta es que el uso de parámetros de asterisco no limita el uso de otros parámetros. 

### Args pt2

Cuando se tiene un parámetro con asterisco y parámetros adicionales los que hace Python es tomar los valores según la posición y todos los demás argumentos que se pasan a partir de la posición del argumento "*args"  se guardan en la tupla.

```
def conbinacion(v1, v2, *args):
    print(v1)
    print(v2)
    print(args)

conbinacion(10, 20, 1, 56, 80)
```

En este ejemplo anterior la tupla imprimiría:
(1, 56, 80)

Incluso podemos agregar parámetros opcionales además de mandarlos a llamar si es necesario cambiar el valor por defecto.

```
def conbinacion(v1, v2, *args, v4=500):
    print(v1)
    print(v2)
    print(args)
    print(v4)

conbinacion(10, 20, 1, 56, 80, v4=1000)
```

### Conclusión 

El uso de parámetros con asterisco no nos limita al uso de otros parámetros y podemos configurar nuestra función como lo necesitemos.