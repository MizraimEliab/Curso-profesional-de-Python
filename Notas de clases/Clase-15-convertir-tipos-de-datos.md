# Clase 15 - Curso de Python - Convertir tipos de datos

## Notas de clase


### Introducción
Ya que conocemos que mediante la función "input" podemos leer valores por teclado y conociendo que la función siempre retorna el valor obtenido en string.

Ahora que pasa cuando queremos manejar otros tipos de datos obtenidos por la función "input" ahí es cuando debemos manejar otros valores a partir de los string obtenidos.

Un ejemplo claro de este caso es cuando queremos que el usuario capture su edad, este dato debe ser manejado como un entero en lugar de un string.


### Convertir tipos de datos

Para obtener por ejemplo un número entero basándonos en el ejemplo de la edad a partir del string dado por la función "input" podemos hacer uso de la función "int" que genera un valor numérico string a entero.

`edad = input('Ingresa tu edad')`
`edad = int(edad)`
`print(edad)`
`print(type(edad))`

Podemos realizar también la generación de un valor flotante a partir de un string dado por la función "input", por ejemplo, imaginemos que requerimos conocer la altura del usuario, al obtenerla mediante la función "input" podemos crear el nuevo valor flotante mediante el uso de la función "float" que trabaja muy similar a la función "int", es decir le pasamos como parámetro un valor flotante en string y la función "float" nos retornará el valor en tipo flotante.

`altura = input('Ingresa tu altura')`
`altura = float(altura)`
`print(altura)`
`print(type(altura))`

Ahora podemos hacer también la creación de un boolean a partir de un string, esto lo podemos lograr con el operador relacional de igualación para lograrlo.

`autorizacion = input(¿Estás autorizado? (si/no): '')`
`autorizacion = autorizacion == 'si'`
`print(autorizacion)`
`print(type(autorizacion))`

Ya que tenemos los ejemplo se puede realizar un ajuste en el código para ahorrar líneas de código y tener un script más limpio, esto lo podemos lograr gracias a el uso de las funciones con el parámetro de "input" que hará exactamente los mismo pero sin la necesidad de reasignar la variable inicial.

`edad = int(input('Ingresa tu edad: '))`
`altura = float(input('Ingresa tu altura: '))`
`autorizacion = input('¿Estás autorizado? (si/no): ') == 'si'`


### Conclusión 

Con las funciones "int", "float" y el operador de igualación podemos obtener nuestros valores capturados por teclado con su correspondiente tipo de datos para poder manejar de una manera correcta los valores ya que sin su uso obtendríamos todos esos valores en string debido a la función "input".