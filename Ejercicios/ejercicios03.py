#No hay profe y los alumnos darán la clase
#Se debe pedir el nombre y la edad de los compañeros que vinieron hoy a la clase

def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del alumno: "))
        alumno = (nombre,edad)
        compañeros.append(alumno)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(5)
print(f"El profesor será: {profesor} y el asistente será: {asistente}")
