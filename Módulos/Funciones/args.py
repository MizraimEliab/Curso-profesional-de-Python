# función común
def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio([10, 10, 5, 7, 10])
print(resultado)



# args
def promedio(*args):
    print(args)
    print(type(args))
    return sum(args) / len(args)

resultado = promedio(10, 10, 5, 7, 10)
print(resultado)



# Args pt2

def conbinacion(v1, v2, *args, v4=500):
    print(v1)
    print(v2)
    print(args)
    print(v4)

conbinacion(10, 20, 1, 56, 80, v4=1000)




# Kwargs

def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(alan=[10, 10, 8], fernando=[10, 9, 9])

def coninacion(*args, **kwargs):
    print(args)
    print(kwargs)

conbinacion(1, 2, 3, 4, 5, algo=True, palabra='Python')