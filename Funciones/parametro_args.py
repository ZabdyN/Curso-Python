#forma no optima de procesar valores
# def suma(lista):
#     num_sum = 0
#     for numero in lista:
#         num_sum = num_sum + numero
#     return num_sum


# resultado = suma([5,3,9])

#forma optima de sumar valores
def sum_total(numeros):
    return sum([*numeros])

resultado2 = sum_total([5,3,9,10,20,3])
print(resultado2)
    
#lo mismo que arriba pero usando el operador * como parametro
#se debe recordar que * es infinito por lo que debe ir al final (nombre, *numeros) y no puede ser (nombre, *num, apellido)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Zabdy",5,3,9,10,20,3)
print(resultado)

