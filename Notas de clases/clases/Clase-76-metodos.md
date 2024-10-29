# Clase 76 - Curso de Python - Métodos

## Notas de clase

### Introducción
Anteriormente revisamos que en Python podemos tener objetos con distintos atributos, sin embargo, esto en un tiempo puede ocasionar un gran problema si no estandarizamos los atributos.

Lo recomendable es que cuando creemos algún objeto de un mismo tipo de clase este objeto y los demás tengan los mismos atributos, ya que de lo contrario, puede ocasionar problemas en nuestros programas.

Para hacer esa estandarización nos apoyaremos de los métodos.

### Métodos

Para nosotros poder crear métodos en una clase basta con definir funciones dentro del bloque de código de la clase.

```
class Usuario:
    
    def inicializar():
        pass

```

Para que el ejemplo anterior pueda ser un método obligatoriamente nuestra función debe recibir un parámetro el cual hace referencia al objeto en si.

Por convención este parámetro tiene el nombre de "self".

"self" hace referencia al nombre en si del objeto. Ahora nosotros podremos usar "self" para definir nuestros atributos y hacer referencia al objeto.


```
class Usuario:
    
    def inicializar(self):
        self.username = ''
        self.password = ''
```

Estos atributos se van a añadir siempre que llamemos al método "inicializar()".

```
class Usuario:
    
    def inicializar(self):
        self.username = ''
        self.password = ''

user1 = Usuario()
user2 = Usuario()

user1.inicializar()
user2.inicializar()

print(user1.__dict__)
print(user2.__dict__)
```

Como se observa en el ejemplo anterior podemos imprimir el meta atributo "__dict__" de nuestros objetos para ver los atributos que tienen y que fueron inicializados en tiempo de ejecución.

Ahora ambos objetos contienen 2 atributos "username" y "password".

Como el método "inicializar()" solo tiene el parámetro "self" al ser llamado no vamos a colocar parámetro alguno, ya que el parámetro será el objeto y como el objeto ya se define no hay necesidad de indicarlo en los argumentos.

Si quisiéramos inicializar los valores con algún otro dato podríamos mandarle al método 2 parámetros más para que los atributos de instancia tome los valores de los parámetros de la función.

```
class Usuario:
    
    def inicializar(self, username, password):
        # Añadiendo atributos al objeto
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()

user1.inicializar('User1', 'Password1')
user2.inicializar('User2', 'Password2')

print(user1.__dict__)
print(user2.__dict__)
```

Ahora con el ejemplo anterior estaríamos creando objetos que parten de la misma clase con mismos atributos pero diferente valor en el atributo y de esta manera se estandariza los atributos de objetos con la clase en común..

Todos los objeto de clase "Usuario" tendrán 2 atributos, uno sería "username" y el otro sería "password" esto siempre y cuando los objetos llamen al método "inicializar()".



### Conclusión 

Ahora con el ejemplo anterior estaríamos creando objetos que parten de la misma clase con mismos atributos pero diferente valor en el atributo y de esta manera se estandariza los atributos de objetos con la clase en común..

Todos los objeto de clase "Usuario" tendrán 2 atributos, uno sería "username" y el otro sería "password" esto siempre y cuando los objetos llamen al método "inicializar()".
Ahora todos los objetos de tipo "Usuario" van a tener por lo menos 2 atributos (username, password) esto siempre y cuando se mande a llamar al método "inicializar()" .

Aún así aunque estandaricemos los atributos como se ha revisado, no el mejor forma de hacerlo, debido a que Python internamente maneja el método "__init__" y mediante este método seremos capaces de inicializar los atributos de un objeto al momento de instanciarlo por lo tanto ya no habrá necesidad de usar métodos que nos permitan inicializar atributos.