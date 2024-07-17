# def frase(nombre,apellido,adjetivo):
#     return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

# frase_resultante = frase("Zabdy","Noguez","verde")
# print(frase_resultante)

#creando la misma funcion con un parametro opcional y un valor por defecto

def frase(nombre,apellido,adjetivo = "Verde"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante = frase("Zabdy","Noguez","Rojo")
print(frase_resultante)
#si el parametro opcional no es modificado o introducido mantiene el valor por defecto con el que fue inicializado
