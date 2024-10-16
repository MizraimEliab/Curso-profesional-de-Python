# Clase 67 - Curso de Python - Decoradores pt2

## Notas de clase

### Introducción
Ahora que pasa si la función a decorar recibe argumentos y retorna algún tipo de valor, en esos casos debemos adaptar a nuestro decorador para que pueda trabajar argumentos y retornar valores.

### Decoradores pt2

Veamos como podemos hacer la adaptación.

```
# Estructura base de un decorador
def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        #pass
        #print('Hola desde la función c')
        print('>>>>> Antes del llamado')
        respuesta = funcion_b(*args, **kwargs)
        print('>>>>> Después del llamado')
        return respuesta
    
    return funcion_c

# Decoradores pt2

@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2

resultado = suma(10, 50)
print(resultado)
```

Como se puede observar en el ejemplo anterior al pasar parámetros en la función a decorar (suma - función b) y retornar un valor deberemos tener los parámetros de *args y **kwargs en la función decorada (función c) además de retornar el llamado de función b que es la función a decorar, de lo contrario obtendremos un error.

El decorador debe ser la suficientemente flexible para recibir una cantidad n de argumentos y en caso de que la función retorne un valor, la función decorada sea capaz de retornar dicho valor.

Cuando llamemos a una función decorada no estaremos llamando a la función como tal, si no que estaremos ejecutando al decorador, si el decorador usa nuestra función veremos el valor retornado.


### Conclusión 

Los decoradores pueden ser aún más complejos ya que hay decoradores para métodos, para clases, etc.