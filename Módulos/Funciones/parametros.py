# usando parámetro con valor por defecto
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)

resultado = area_circulo(10)
print(resultado)


# usando actualización de parámetro con valor por defecto
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)

resultado = area_circulo(10, 3.141592)
print(resultado)

# usando nombres en ejecución de la función sin importar la posición
def area_circulo(radio, pi=3.1416):
    return pi * (radio ** 2)

resultado = area_circulo(pi=3.141592, radio=10)
print(resultado)