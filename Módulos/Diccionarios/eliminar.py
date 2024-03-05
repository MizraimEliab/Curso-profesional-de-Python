diccionario = {'a': 1, 'b':2, 'c':3, 'd':4}

print(len(diccionario))

del diccionario['a'] # 1
val = diccionario.pop('b') # 2


print(val)
print(diccionario)
print(len(diccionario))


# borra todos los elementos
diccionario.clear() # 3
print(diccionario)