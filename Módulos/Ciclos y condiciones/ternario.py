calificacion = 10
color = None

if calificacion >= 7:
    color = 'verde'
else:
    color = 'rojo'

print(calificacion, color)


color = 'verde' if calificacion >=7 else 'rojo'

print(calificacion, color)