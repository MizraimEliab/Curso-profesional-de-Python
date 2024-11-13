# Clase 75 - Curso de Python - Atributos dinámicos

## Notas de clase

### Introducción
En Python podemos añadir de manera dinámica atributos a nuestros objetos.

Recordando que tenemos nuestros atributos de clase y los atributos de instancia que estos últimos son almacenados en el meta atributo "__dict__".

### Atributos dinámicos

Vamos a revisar como añadir atributos a nuestros objetos de manera dinámica.

```
user1.username = 'Beto'
print(user1.username)
```

Como se puede ver en el ejemplo anterior añadimos de manera dinámica el atributo al objeto "user1" mediante la asignación del objeto y sui atributo a un valor.

Ya que Python detecta que el objeto se le agrego un atributo de manera dinámica en tiempo de ejecución y este atributo se convierte en un atributo de instancia por lo tanto será almacenado en nuestro meta atributo "__dict__".

De esta manera podemos añadir la cantidad de atributos a nuestro objeto que necesitemos de manera dinámica y Python al detectar estos nuevos atributos los creará en el objeto.

También podemos modificar estos atributos fácilmente en tiempo de ejecución reasignando el valor del atributo.

```
user1.password = '1234'

print(user1.password)

user1.password = 'password'
print(user1.password)
```

Los atributos de instancia son exclusivos de cada objeto ya que si declaramos otro objeto aunque parta de la misma clase y queremos acceder a un atributo del objeto 1 en el objeto 2 Python nos mandará un error.

### Conclusión 

Es posible añadir atributos de manera dinámica que son atributos de instancia ya que son atributos que cuentan los objetos.