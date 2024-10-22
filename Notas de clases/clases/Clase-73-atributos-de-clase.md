# Clase 73 - Curso de Python - Atributos de clase

## Notas de clase

### Introducción
Algo interesante de Python es que podremos dividir los atributos en 2 tipos, los atributos de clases y los atributos de instancia.

### Atributos de clase

Los atributos de clase son atributos los cuales les pertenezcan a una clase y para usarlos tenemos que usar dicha clase, por otro lado los atributos de instancia son atributos que le pertenecen a un objeto y para usarlos obligatoriamente debemos trabajar con el objeto.

Para crear los atributos de clase es bastante sencillo, basta con crear variables dentro de la clase.

```
class Usuario:
    username = ''
    email = ''
```

De esta manera como se muestra en el ejemplo anterior podremos crear atributos de clase, solo basta con definir variables dentro de la clase, estos atributos le pertenecen a la clase y para usarlos debemos usar la clase.

Esto se puede comprobar imprimiendo un atributo de la clase.

```
class Usuario:
    username = 'Hola mundo soy una clase'
    email = ''

print(Usuario.username)

```
De esta manera como es mostrada en el ejemplo anterior podremos usar las atributos de clase llamando a las clase seguido de un punto y el atributo de la clase ya sea para lectura o escritura.

Podemos escribir el atributo de clase y modificarlo solo basta reasignando el atributo llamando a la clase y volviendo a imprimir los atributos de clase.

```
class Usuario:
    username = 'Hola mundo soy una clase'
    email = ''

Usuario.username = 'Usuario 1'
Usuario.email = 'usuario@email.com'

print(Usuario.username)
print(Usuario.email)
```


### Conclusión 

Para poder definir atributos de clase bastará con solamente definir variables dentro de la clase.