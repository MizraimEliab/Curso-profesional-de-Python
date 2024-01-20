mensaje = 'Hola Mundo!'

# ljust -> Alinea el texto a la izquierda
# rjust -> Alinea el texto a la derecha
# center -> Alinea el texto al centro

mensaje = mensaje.ljust(20)
print(mensaje, '.')

mensaje = mensaje.rjust(20)
print(mensaje, '.')

mensaje = mensaje.center(20)
print(mensaje, '.')