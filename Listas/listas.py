#                   0         1        2       3       4        ---> Indices
#                  -5        -4       -3      -2      -1        <--- Indices
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']

primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)

# Lectura de la lista de forma inversa derecha a izquierda
ultimo_curso = lista_cursos[-1] # 4
print(ultimo_curso)

tercer_curso = lista_cursos[-3] # 2
print(tercer_curso)

# actualizando valores de la lista
lista_cursos[-1] = 'Rust'
print(lista_cursos)

# Sublistas en Python

# [start:end]
# [start:] -> Obtenemos los últimos elementos de la lista
# [:end] -> Obtenemos los primeros elementos de la lista
# [start:end:step] -> Obtenemos los elementos de la lista con un salto

sub_lista = lista_cursos[0:3] # [0, 3]
print(sub_lista)

sub_lista = lista_cursos[1:] # [1, 4]
print(sub_lista)

sub_lista = lista_cursos[:4] # [0, 3]
print(sub_lista)

# Podemos agregar un tercer parámetro que es el salto en nuestra lista
sub_lista = lista_cursos[1:4:2] # [1, 4, 2]
print(sub_lista)


# Agregar elementos a una lista
# append -> Agrega un elemento al final de la lista
# insert -> Agrega un elemento en una posición específica de la lista y recorrerá los demás elementos

lista_cursos.append('Rust')
lista_cursos.append('Go')
print(lista_cursos)

print(len(lista_cursos))


lista_cursos.insert(0, 'C#')
print(lista_cursos)


# Extender una lista con otra lista

lista_cursos_2 = ['C++', 'C', 'Docker']

lista_cursos.extend(lista_cursos_2)
print(lista_cursos)
print(lista_cursos_2)

# Eliminar elementos de una lista
# pop -> Elimina el último elemento de la lista
# remove -> Elimina un elemento específico de la lista
# del -> Elimina un elemento específico de la lista

lista_cursos.remove('C#')
print(lista_cursos)

del lista_cursos[0]
print(lista_cursos)

lista_cursos.pop()
print(lista_cursos)

# Eliminar todos los elementos de una lista
lista_cursos.clear()
print(lista_cursos)

# Ordenar una lista
lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
lista.sort()
print(lista)
# Ordenar una lista de forma inversa
lista.sort(reverse=True)
print(lista)

# Conocer el menor y mayor valor de una lista
print(min(lista))
print(max(lista))

# Conocer si un elemento se encuentra en una lista
print(10 in lista)

# Conocer si un elemento no se encuentra en una lista
print(11 not in lista)





