# Variables no locales
e = 'e' # Variable global

def funcion_principal():
    a = 'a' # Variable local
    b = 'b' # Variable local

    def funcion_anidada():
        c = 'c' # Variable local
        nonlocal b
        b = 'Cambio de valor'
        print(a)
        print(b)
        print(e)

    funcion_anidada()
    print(c)

funcion_principal()

# Retornar funciones

def saludar():

    def mostrar_mensaje():
        print('Hola nos encontramos de nuevo!')
    return mostrar_mensaje

respuesta = saludar()
print(respuesta)
print(type(respuesta))

respuesta()

# Closures

def saludar(username):
    mensaje = f'Hola {username}' # Variable local

    def mostrar_mensaje(): # Anidada
        print(mensaje)
    return mostrar_mensaje

username = 'Alan'
respuesta = saludar(username)

respuesta()