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


# Métodos

class Usuario:
    # __init__
    def inicializar(self, username, password):
        # Añadiendo atributos al objeto
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()

user1.inicializar('User1', 'Password1')
user2.inicializar('User2', 'Password2')

print(user1.__dict__)
print(user2.__dict__)


# Método init

class Usuario:
    # __init__
    def __init__(self, username='', password=''):
        print('Se esta crendo un usuario')
        self.username = username
        self.password = password

user1 = Usuario('user1', 'pass1')
user2 = Usuario('user2', 'pass2')
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)