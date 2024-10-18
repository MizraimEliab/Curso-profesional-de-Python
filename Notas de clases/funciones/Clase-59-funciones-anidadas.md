# Clase 59 - Curso de Python - Funciones anidadas

## Notas de clase

### Introducción
Al igual que las condiciones y los ciclos en Python también las funciones pueden ser anidadas, es decir, funciones pueden poseer a la vez otras funciones

### Funciones anidadas

Para ver las funciones anidadas podemos verlo con un ejemplo de operación bancaria, donde siempre existen retiros y depósitos de dinero.

```
def operacion():

    def deposito(cantidad, balance):
        return cantidad + balance
    

    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance  - cantidad
        else:
            return None
    
    print(deposito(10, 20))
    print(retiro(50, 80))


operacion()
```

En el ejemplo se puede notar que se definen 2 funciones dentro de otra función y para poder ver un resultado se imprime el llamado de las 2 funciones dentro de la función principal para que de esta manera al llamar a la función principal se muestren los resultados de las funciones anidadas.

A su vez las funciones anidadas que vemos en el ejemplo pueden tener más funciones anidadas ya que podemos tener funciones anidadas hasta n cantidad de niveles.

Podemos hacer un reestructuración del código anterior y hacer el uso de parámetros para usarlos en las funciones anidadas.

```
def operacion(cantidad, balance, tipo='deposito'):

    def deposito(cantidad, balance):
        return cantidad + balance
    

    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance  - cantidad
        else:
            return None
    
    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)


resultado = operacion(50, 100)
print(resultado)
```

### Conclusión 

Se observa que el uso de las funciones anidadas pueden ser de utilidad en determinados casos de uso y que la implementación de estas funciones anidadas es literalmente definir una función dentro de otra función.

Lo común es tener funciones anidadas de 2 niveles, sin embargo, podemos tener más niveles si es que se requiere.