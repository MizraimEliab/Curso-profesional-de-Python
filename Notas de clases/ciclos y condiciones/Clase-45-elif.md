# Clase 45 - Curso de Python - elif

## Notas de clase

### Introducción

Algo común al querer ejecutar nuestro programa es evaluar diferentes condiciones para poder así ejecutar diferentes bloques de código para lograr esto se hace uso de la palabra reservada "elif".

### elif

Para la evaluación de diferentes condiciones haremos uso de la palabra reservada "elif" y veremos un ejemplo de como ejecutar diferentes bloques de código.

Para este ejemplo haremos la muestra de un mensaje dependiendo de la calificación que haya obtenido un alumno.

```
calificacion = 8

if calificacion == 10:
    print('Felicidades, aprobaste la materia con una calificación perfecta')
elif calificacion == 9 or calificacion== 8:
    print('Ferlicidades, aprobaste la materia')
elif calificacion == 7 or calificacion == 6:
    print('Aprobaste la materia')
else:
    print('Reprobaste la materia')
```

La palabra reservada se evalúa después de la primera condición "if" cuando se requiere evaluar más de una condición sin que se llegué a la acción contraria de la primer condición, esto quiere decir antes de la evaluación del "else".

Las evaluación se ejecuta de manera descendente iniciando por "if", luego "elif" y al final el "else" y se van descartando una por una si el resultado de la evaluación es falso.

De esta manera se evalúan múltiples condiciones.

### Conclusión 

Con las condicionales múltiples podemos evaluar distintos escenarios dentro de un  caso que exija diferentes condiciones y no este limitado a solamente 1 condición y el contrario a dicha condición.