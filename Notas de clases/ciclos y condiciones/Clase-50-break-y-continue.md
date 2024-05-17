# Clase 50 - Curso de Python - Break y Continue

## Notas de clase

### Introducción
Existen 2 palabras reservadas que nos permitirán cambiar el comportamiento de nuestros ciclos, es decir para "for" y "while".

Estas 2 palabras reservadas son "break" y "continue".

### Break y Continue

Para ver el cambio de comportamiento con ambas palabras reservadas se revisará un ejemplo.

Vamos a iterar sobre un string para obtener sus caracteres.

```
titulo_curso = 'Curso profesional de Python'

for caracter in titulo_curso:

    if caracter == 'P':
        break
    
    print(caracter)

```
En este ejemplo podemos observar que contamos con doble bloque donde cada bloque de código cuenta con sus respectiva identación y además podemos ver que dentro del ciclo estamos condicionando a que si en nuestra frase string existe una letra "P" va a usar la palabra reservada "break" que lo que hará será finalizar el ciclo si la condición previa de cumple.

La palabra reservada permite finalizar de manera inmediata un ciclo "for" y un ciclo "while".

Ahora veamos otro ejemplo.

```
titulo_curso = 'Curso profesional de Python'

for caracter in titulo_curso:

    if caracter == 'P':
        continue
    
    print(caracter)
```

En este ejemplo se muestra el mismo código de ejemplo anterior solamente cambiando la palabra reservada "break" por "continue" y en este ejemplo usando "continue" imprimirá cada caracter excepto la "P", esto se debe a que "continue" salte a la siguiente iteración.

"continue" brinca la iteración y pasa a la siguiente.



### Conclusión 

Esta palabras reservada "break" y "continue" son las que nos permiten cambiar el comportamiento dentro de nuestros ciclos.