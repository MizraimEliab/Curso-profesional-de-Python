nombre = 'Alex' or 'Alan'

print(nombre)

nombre = '' or 'Alan'

print(nombre)


nombre = '' or 0 or [] or True

print(nombre)

listado = []
nombre = 'Dante'

if listado:
    nombre = listado
else:
    nombre = nombre

print(nombre)


nombre = nombre or listado
print(nombre)