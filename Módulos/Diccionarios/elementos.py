diccionario = {'a': 1, 'b':2, 'c':3, 'd':4}

print('a' in diccionario)

valor = diccionario['d']
print(valor)

# get

valor = diccionario.get('d')
print(valor)

valor = diccionario.get('z', 'La llave no existe')
print(valor) # 'La llave no existe'

#setdefault
valor = diccionario.setdefault('e', 5)
print(valor) # 5