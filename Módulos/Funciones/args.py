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