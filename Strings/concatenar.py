nombre = 'Alan Isaac'
apellido = 'Turing'


nombre_completo = nombre + ' ' + apellido + '.'
print(nombre_completo)

nombre_completo = 'Sr. %s %s.' % (nombre, apellido)
print(nombre_completo)

# concatenar pt2 

nombre_completo = 'Mr. {} {}.'.format(nombre, apellido)
print(nombre_completo)

nombre_completo = 'Mr. {name} {last_name}.'.format(name=nombre, last_name=apellido)
print(nombre_completo)

# FStrings
nombre_completo = f'Mr. {nombre} {apellido}.'
print(nombre_completo)

nombre_completo = f'Mr. {nombre} {apellido} {'Arch'}.'
print(nombre_completo)