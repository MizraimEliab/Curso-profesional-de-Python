# Función para calcular el promedio
promedio = lambda *args : sum(args) / len(args)

print(promedio(10, 10, 9, 8, 7))

# Función para ver si un estudiante aprobó basandose en su calificación promedio
aprobatorio  = lambda calificacion : calificacion >= 7

print(aprobatorio(7))

# Función principal de mostrar mensaje para usar los callbacks es decir usar la funciones lambda de promedio y aprobatorio

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades aporbaste la materia con {promedio}')
    else:
        print('No aprobaste la materia')


mostrar_mensaje(promedio, aprobatorio, *args)