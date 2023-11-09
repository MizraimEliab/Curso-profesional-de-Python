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



