# Clase 62 - Curso de Python - Callbacks

## Notas de clase

### Introducción
Los callbacks son funciones que son utilizadas como argumentos para otras funciones y serán las funciones que reciban estos argumentos las cuales las llamen.

### Callbacks

Vamos a revisar un ejemplo de callbacks con una función lambda que nos permita obtener el promedio de cualquier listado.

```
promedio = lambda *args : sum(args) / len(args)
print(promedio(10, 10, 9, 8, 7))
```

Ya que tenemos nuestra función que calcula el promedio de una tupla de números que perfectamente podemos usar para determinar las calificaciones de un estudiante.

Entonces ahora haremos otra función para determinar si un estudiante aprobó o reprobó una materia basándose en su promedio. 

Para que el estudiante apruebe la materia su calificación debe ser mayor o igual a 7.

```
aprobatorio  = lambda calificacion : calificacion >= 7
print(aprobatorio(7))
```

Ahora para ver los callbacks en funcionamiento se hará una tercera función que muestre un mensaje más personalizado para determinar si un estudiante aprobó o no en base a su promedio usando los valores que retornan las 2 primeras funciones.

```
def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades aporbaste la materia con {promedio}')
    else:
        print('No aprobaste la materia')


mostrar_mensaje(promedio, aprobatorio, *args)
```

Como podemos observar las funciones lambda que creamos previamente son los callbacks de esta función principal porque son funciones que se llaman dentro de la función principal.

Con esto hemos divido el ejercicio en pequeñas funciones, una función calcula el promedio, otra determina si ese promedio es aprobatoria o no y la función principal muestra un mensaje.

### Conclusión 

Los callbacks son de mucha utilidad en programas que son modulares y se puedan generar funciones que puedan ser empleadas en otras funciones principales.  