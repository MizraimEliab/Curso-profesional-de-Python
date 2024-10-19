def suma(numero_uno, numero_dos):
    return numero_uno + numero_dos, 'Función ejecutada correctamente'

numero_uno = int(input('Ingresa el primer número entero:'))
numero_dos = int(input('Ingresa el segundo número entero:'))

resultado, mensaje = suma(numero_uno, numero_dos)
print("El resultado de la suma es: ", resultado)
print("El mensaje es: ", mensaje)