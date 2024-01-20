# Busqueda de caracteres en un string con count()
titulo_curso = 'Curso profesional de Python'

contador = titulo_curso.count('Python')
print(contador)

# Buscar mediante in
print('Python' in titulo_curso)

print('python' in titulo_curso.lower())
print('alan' not in titulo_curso.lower())
print('PYTHON' in titulo_curso.upper())

# Buscar mediante find()
print(titulo_curso.find('Python'))
print(titulo_curso.find('python'))

# Buscar mediante srartswith() y endswith()
print(titulo_curso.startswith('Curso'))
print(titulo_curso.startswith('curso'))
print(titulo_curso.endswith('Python'))
print(titulo_curso.endswith('python'))

