# Docstring
# __doc__ (Módulos, Clases, Métodos, Funciones)

def suma(numero_uno, numero_dos):
    """
    La función suma dos números enteros.

    Argumentos:
    numero_uno (int)
    numero_dos (int)

    Se retorna la suma de los parámetros.
    """
    return numero_uno + numero_dos

print(suma.__doc__)
print(help(suma))