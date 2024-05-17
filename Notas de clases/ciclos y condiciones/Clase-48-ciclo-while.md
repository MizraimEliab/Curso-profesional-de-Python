# Clase 48 - Curso de Python - Ciclo while

## Notas de clase

### Introducción
Un ciclo no permite ejecutar n cantidad de veces un bloque de código hasta que una condición se cumpla o bien hasta que n llegué a un límite.

Particularmente el ciclo "while" ejecuta un bloque de código n cantidad de veces hasta que una condición se cumpla.

### Ciclo while

Veamos un ejemplo del uso de "while" en este caso solo haremos que se muestre por pantalla la sucesión numérica del 1 al 10.

```
contador = 1

while contador <= 10:
    print(contador)
    contador += 1
```

Para este ejemplo usamos una variable contador que vamos incrementando de 1 unidad en unidad para hacer la sucesión, sien embargo, dada la condición del ciclo "while" cuando el valor de contador sea 11, la condición deja de cumplirse y por lo tanto termina la iteración del ciclo.

El ciclo "while" es bueno usarlo cuando no conozcamos la cantidad de iteraciones que se van a necesitar o requerir, revisemos un ejemplo de ello.

Vamos ha hacer un ejemplo donde se cuenten los dígitos de un número entero.

```
numero = 1234
contador_digitos = 0

while numero >= 1:
    contador_digitos += 1

    numero = numero / 10

print(contador_digitos)

```

En este ejemplo como no se conoce el número de iteraciones debido a que puede variar el número de dígitos de entrada se convierte en un buen ejemplo del ciclo "while".

Pro Tip:

El incremento de una variable se puede usar con abreviatura como se muestra en los ejemplos.

Con el ciclo "while" opcionalmente podemos usar la sentencia "else" para indicarle que hacer al ciclo cuando la condición no se cumple, esto similar a como trabaja el "if".

```
numero = 1234
contador_digitos = 0

while numero >= 1:
    contador_digitos += 1

    numero = numero / 10
else:
    print('Fin del ciclo while')

print(contador_digitos)
```



### Conclusión 

Con el ciclo "while" podemos iterar basandonos en una condición hasta que esta se cumpla y con ello podemos repetir n veces un bloque de código, adicionalmente podemos indicar al igual que el "if" que hacer cuando nuestra condición sea falsa.