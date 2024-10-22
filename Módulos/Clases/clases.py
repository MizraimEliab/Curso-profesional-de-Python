# Clases
class Usuario:
    pass

eliab = Usuario()
print(eliab)

# Atributos de clase

# Attrs de clase
# Attrs de instancia

class Usuario:
    # Attrs de clase
    username = 'Hola mundo soy una clase'
    email = ''

Usuario.username = 'Usuario 1'
Usuario.email = 'usuario@email.com'

print(Usuario.username)
print(Usuario.email)