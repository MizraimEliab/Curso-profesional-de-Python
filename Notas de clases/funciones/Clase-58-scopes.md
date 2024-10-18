# Clase 58 - Curso de Python - Scopes

## Notas de clase

### Introducción

En esta lección se revisará como se comportan las variables tanto fuera como dentro de las funciones, esto es importante tenerlo en cuenta debido a que debemos conocer como se comportan nuestras variables en nuestro programa.



### Scopes

Nos apoyaremos del siguiente código para la explicación de los scopes:

```
animal = 'Gato'

def imprimir_animal():
    print(animal)

imprimir_animal()

```

En el código se puede observar que se tiene una variable y una función la cual unicamente se encarga de imprimir por consola dicha variable.

Si se ejecuta el siguiente código la consola nos regresará "Gato" como resultado, sin embargo, si nosotros modificamos la variable animal dentro de la función antes de imprimir la variable obtendremos el resultado de la variable animal dentro de la función pero OJO la variable inicial que se define antes de la función no cambiará su valor.

```
animal = 'Gato'

def imprimir_animal():
    animal = 'Perro'
    print(animal)

imprimir_animal()

print(animal)

# Perro
# Gato
```

Esto se debe al tema de Scope, para Python en el ejemplo anterior las variables animal aunque parecen ser la misma variable para Python no lo es porque se encuentran en un alcance diferente.

La  primer variable al no estar dentro de un bloque de código se considera como una variable global, las variables globales pueden ser usadas dentro de cualquier bloque de código, como una función, ciclo o condición.

Por otra parte la variable que se encuentra dentro de la función con el mismo nombre de la variable global será conocida como variable local y esta variable solo puede ser usada dentro del bloque donde fue creada.

Aunque las variables cuenten con el mismo nombre son objetos diferentes ya que poseen alcances diferentes y así es como lo entiende Python, esto incluso se puede comprobar imprimiendo los identificadores de los objetos con la función "id()" para conocer dichos identificadores.

```
animal = 'Gato' # Variable Global -> Función, Condición o Ciclo

def imprimir_animal():
    animal = 'Perro' # Variable Local
    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))
```


Otra prueba que podemos emplear es tratar de imprimir una variable local fuera de su bloque, en este caso una función, esto nos regresará un error de variable no definida debido al alcance de la misma variable.

```
animal = 'Gato' # Variable Global -> Función, Condición o Ciclo

def imprimir_animal():
    animal = 'Perro' # Variable Local
    print(animal)
    print(id(animal))

    tipo = 'Canino'

imprimir_animal()

print(animal)
print(id(animal))
print(tipo)

# NameError: name 'tipo' is not defined

```

Finalmente en caso de que sea necesario modificar el valor de una variable global dentro de un bloque de código como una función se deberá emplear la palabra reservada "global" que se usará como prefijo de la variable global.

```
animal = 'Gato' # Variable Global -> Función, Condición o Ciclo

def imprimir_animal():
    global animal
    animal = 'Perro'
    #animal = 'Perro' # Variable Local
    print(animal)
    print(id(animal))

    tipo = 'Canino'

imprimir_animal()

print(animal)
print(id(animal))
```

Con el ejemplo anterior le estamos diciendo a Python que queremos usar la variable global para modificarla dentro de la función.

### Conclusión 

Las variables que tengamos fuera de un bloque de código como una función, condición o ciclo las conoceremos como variables globales y aquellas variables que se encuentren dentro de un bloque de código las conoceremos como variables locales donde la principal diferencia entre ambas variables será el alcance que tiene la variable dentro del programa.