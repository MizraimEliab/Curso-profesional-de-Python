# Clase 46 - Curso de Python - Ternario

## Notas de clase

### Introducción
Se establece un caso donde se tienen que evaluar calificaciones de alumnos, el alumno aprobará si y solo si cuenta con una calificación igual o mayor a 7 puntos de lo contrario el alumno obtendrá una calificación reprobatoria.

Pintaremos de un color la calificación aprobatoria y reprobatoria, verde para aprobado y rojo para reprobado.

### Ternario

En base al escenario anterior usaremos 2 variables la calificación y el color.

Podemos hacer uso de un "if" para resolver el escenario planteado junto a las 2 variables anteriormente mencionadas mediante el siguiente código.

```
calificacion = 10
color = None

if calificacion >= 7:
    color = 'verde'
else:
    color = 'rojo'

print(calificacion, color)
```

Este ejemplo funciona, pero el escenario es simple para tantas líneas de código ya que podemos usar el equivalente al ternario en Python y haciendo una reestructuración de este código en menos líneas como se muestra a continuación.

```
color = 'verde' if calificacion >=7 else 'rojo'

print(calificacion, color)
```



### Conclusión 

Como se puede observar podemos cambiar la estructura del código para solucionar el escenario, en este caso la condición se cambió a una sola línea de código y se obtuvo el mismo resultado.

Como nota importante el "else" cuando se usan múltiples líneas para el bloque condicional se vuelve opcional, sin embargo, cuando la condición solamente se mantiene en una línea es obligatorio.