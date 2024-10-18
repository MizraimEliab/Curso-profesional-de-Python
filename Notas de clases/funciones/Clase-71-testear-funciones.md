# Clase 71 - Curso de Python - Testear funciones

## Notas de clase

### Introducción
Algo muy interesante de Python es que podemos testear nuestra funciones usando el "Docstring" , es decir, podemos comprobar el comportamiento de una función únicamente con comentarios.

### Testear funciones

Veamos como.

```
def suma(numero_uno, numero_dos):
    """
    La función suma dos números enteros.

    Argumentos:
    numero_uno (int)
    numero_dos (int)

    Se retorna la suma de los parámetros.

    >>> suma(10, 15)
    25

    >>> suma(25, 25)
    50
    """
    return numero_uno + numero_dos
```

Como podemos observar en el ejemplo dentro del "Docstring" vamos a agregar triple mayor que seguido del llamado de la función con sus respectivos argumentos y luego una línea abajo el resultado esperado o el resultado correcto de la función.

Podemos tener n cantidad de pruebas en nuestro "Docstring" sin embargo, se recomienda por legibilidad mantener máximo 3 pruebas.

Finalmente para ejecutar nuestra prueba deberemos hacer uso del siguiente comando.

```
python -m doctest <nombre del archivo> .py
```

Al usar el módulo "doctest" lo que Python hará será probar los objetos documentados a través de su "Docstring".

Al ejecutar el comando si Python no nos regresa nada será un indicador de que todos los test se ejecutaron correctamente y no se encontraron fallas.

En caso de que pongamos un valor erróneo como el esperado y volvemos a ejecutar el comando obtendremos un error y con esto confirmamos que "doctest" esta probando nuestras funciones usando el "Docstring".


### Conclusión 

Gracias al módulo de "doctest" haciendo uso del "Docstring" seremos capaces de testear las funciones que tengamos documentadas.

Esto tiene la ventaja de que aparte de tener documentadas nuestras funciones las podemos testear sin la necesidad de librerías adicionales.