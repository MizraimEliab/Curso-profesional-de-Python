# Clase 77 - Curso de Python - Método init

## Notas de clase

### Introducción
En Python para que podamos definir e inicializar atributos para un objeto al momento de crearlo se hará uso del método "init".

### Método init

Vamos a ver un ejemplo de como podemos sobre escribir el método "init" y se hace la mención de la palabra sobre escribir debido a que todas las clases en Python heredan de la clase "Object" que a su vez posee el método "init".

El método "init" se va a llamar cuando instanciemos un objeto.

```
class Usuario:
    # __init__
    def __init__(self, username, password):
        print('Se esta crendo un usuario')
        self.username = username
        self.password = password

user1 = Usuario('user1', 'pass1')
user2 = Usuario('user2', 'pass2')

print(user1.__dict__)
print(user2.__dict__)
```

De esta manera como se ve en el ejemplo anterior seremos capaces de inicializar nuestros atributos sobre escribiendo el método "init" y tendremos la diferencia de que no tenemos que mandar a llamar al método desde el objeto basta con pasarle los parámetros a la instancia de la clase.

Usando el método "init" seremos capaces de definir e inicializar atributos para nuestros objetos.

Dentro del método "init" se pueden establecer los valores en argumentos por default como cualquier otra función en Python.


```
class Usuario:
    # __init__
    def __init__(self, username='', password=''):
        print('Se esta crendo un usuario')
        self.username = username
        self.password = password

user1 = Usuario('user1', 'pass1')
user2 = Usuario('user2', 'pass2')
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
```


### Conclusión 

El método "init" se va a llamar cuando el objeto sea instanciado y mediante este método seremos capaces de definir la cantidad y nombres de atributos que poseerán los objetos.