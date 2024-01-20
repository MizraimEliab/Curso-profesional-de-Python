lenguajes = 'Python Ruby Java Rust C++ C'

listado_lenguajes = lenguajes.split() # divide el string en una lista por default con espacios
print(listado_lenguajes)

lenguajes = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes = lenguajes.split('-') # divide el string a partir de todas las coincidencias del caracter
print(listado_lenguajes)

lenguajes = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes = lenguajes.split('-', 2) # divide el string a partir de todas las coincidencias del caracter y opcionalmente se le puede indicar el numero de divisiones
print(listado_lenguajes)


lenguajes = ['Python', 'Ruby', 'Java', 'Rust']

string_lenguajes = ' '.join(lenguajes) # une los elementos de la lista con el caracter indicado
print(string_lenguajes)
print(type(string_lenguajes))