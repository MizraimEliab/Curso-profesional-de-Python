# * -> Resto de valores en lista
# _ -> Omitir valores
numeros = (1, 2, 3, 4)
uno, dos, tres, cuatro = 1, 2, 3, 4
uno, dos, tres, cuatro = numeros

# Tomar los primeros valores y el resto en una lista
uno, dos, tres, *resto_valores = numeros

# Ignorar valores restamntes
uno, dos, tres, *_ = numeros

# Ignorar valores pero tomar los últimos de la tupla
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *_, nueve, diez = numeros

print(uno)
print(dos)
print(tres)
# print(cuatro)
print(resto_valores)
print(nueve)
print(diez)