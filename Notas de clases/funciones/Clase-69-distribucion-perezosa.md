# Clase 69 - Curso de Python - Distribución perezosa

## Notas de clase

### Introducción
Pensando en que sin uso de generador podríamos retornar una lista con los elementos obtendríamos un resultado similar a un generador, pero, la ventaja del uso de los generadores recae en la forma en la que iteramos los elementos que nos proporciona el generador.

Al usar el generador podremos pausar la ejecución de generador obteniendo una iteración perezosa (Lazy iterator) obteniendo los elementos que nos regresa el generador bajo demanda.  

### Distribución perezosa

Una ventaja importante es el uso de memoria ya que al obtener solamente los valores que necesitemos y cuando los necesitemos no estaremos reservando espacio en memoria que no usaremos.

Esto nos ayuda mucho trabajando con miles o millones de registros.

Para que quede más claro el concepto de distribución perezosa veremos un ejemplo haciendo uso de la función "next()".


```
generador = pares()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
```

Con el código anterior podremos obtener los elementos de generador "pares()" bajo demanda haciendo uso de la función "next()" que nos ayuda a pasar al siguiente elemento del generador.

Nosotros vamos a consumir el generador siempre que lo necesitemos y esto hace una iteración perezosa.

Evidentemente pudiéramos ejecutar diferentes sentencias de código entre una y otra ejecución del generador, logrando un mejor uso de la información bajo demanda que nos brinda el generador.

```
generador = pares()
print(next(generador))

print(next(generador))

print(next(generador))

print('Ejcutamos código entre un llamado y otro')

print(next(generador))

```

Cuando el generador haya finalizado con el uso de los llamados que hagamos con la función "next()" Python nos mostrará un error que indique que la iteración se detuvo.

Este error lo podemos manejar con "try / except" para validar este paro de iteración.

```
while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo.')
        break
```


### Conclusión 

Los generadores nos permiten tener valores bajo demanda por el pausa de la función e iterarlos para emplearlos cuando se requieran dichos valores, esta iteración se le conoce como iteración perezosa y nos ayuda a optimizar memoria además de trabajar solamente con los datos que se ocupen.