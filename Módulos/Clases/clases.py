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

# Atributos de instancia

# __dict__

class Usuario:
    # Attrs de clase
    username = 'Hola mundo soy una clase'
    email = ''

user1 = Usuario()
# 	1. Verifica si el atributo existe dentro del objeto.
#	2. Verifica si el atributo existe dentro de la clase (Solamente funciona para lectura).
#   3. Lanzar un error.
print(user1.username)

print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__) # Dict


# Atributos dinámicos

user1.username = 'Beto'
user1.password = '1234' # Añadimos el atributo al objeto y se convierte en un atributo de instancia
print(user1.username)
print(user1.password)

user1.password = 'password'
print(user1.password)