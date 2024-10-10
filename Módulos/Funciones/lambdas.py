# Funciones cuidadanas de primera clase
def centigrados_a_fahrenheit(grados):
    return grados * 1.8 + 32

print(centigrados_a_fahrenheit(10))
print(centigrados_a_fahrenheit(-1))
print(centigrados_a_fahrenheit(8))


mi_funcion = centigrados_a_fahrenheit
print(type(mi_funcion))

print(mi_funcion(10))

# Funciones lambda

# lambda <parámetros> : <Cuerpo de la función>
funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(16))

"""
sin_parametros = lambda : True
parametros_default = lambda a1=10, a2=20, a3=30 : a1 + a2 + a3
asterisco = lambda *args, **kwargs : len(args) + len(kwargs)

"""