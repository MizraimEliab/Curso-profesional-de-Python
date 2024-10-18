# Decoradores
"""
a -> La función principal (Decorador)
b -> La función a decorar
c -> La función decorada

a(b) -> c
"""
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

@funcion_a
def saludar():
    print('Hola Mundo!')

saludar()

# Decoradores pt2

@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2

resultado = suma(10, 50)
print(resultado)