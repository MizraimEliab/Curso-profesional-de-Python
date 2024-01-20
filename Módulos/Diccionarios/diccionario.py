diccionario = {}
diccionario = dict()

# {"llave": "valor"}
diccionario = {"total": 55}
diccionario = {"total": 55, "descuento": True, "subtotal": 15}

diccionario = {"total": 55, 10: "Curso de Python", (1,2,3): True}

# Agregar un elemento
diccionario["curso"] = "Curso de Python"
print(diccionario)

# Modificar un elemento
diccionario["total"] = 60
print(diccionario)

# Acceder a un elemento
print(diccionario["total"])

# Eliminar un elemento
diccionario.pop("descuento")
print(diccionario)

# Obtener todas las llaves
print(diccionario.keys())

# Obtener todos los valores
print(diccionario.values())

# Obtener todos los elementos
print(diccionario.items())

# Usar get
print(diccionario.get("total"))

# usar get si la llave no existe
print(diccionario.get("total2"), [])

# Limpiar
diccionario.clear()

