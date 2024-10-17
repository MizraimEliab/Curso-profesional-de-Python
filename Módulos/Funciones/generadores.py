def pares(): # Generador -> Lazy iterator
    for numero in range(0, 100, 2):
        #return numero
        yield numero # La función suspende su ejecución
        print('Se reanuda la ejecución')

# print(pares())

for par in pares():
    print(par)