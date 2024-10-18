def pares(): # Generador -> Lazy iterator
    for numero in range(0, 100, 2):
        #return numero
        yield numero # La función suspende su ejecución
        print('Se reanuda la ejecución')

# print(pares())

for par in pares():
    print(par)

# Distribución perezosa
generador = pares()
print(next(generador))

print(next(generador))

print(next(generador))

print('Ejcutamos código entre un llamado y otro')

print(next(generador))

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo.')
        break