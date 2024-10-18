# Scope
animal = 'Gato' # Variable Global -> Función, Condición o Ciclo

def imprimir_animal():
    global animal
    animal = 'Perro'
    #animal = 'Perro' # Variable Local
    print(animal)
    print(id(animal))

    tipo = 'Canino'

imprimir_animal()

print(animal)
print(id(animal))
