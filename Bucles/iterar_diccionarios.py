dicionario = {
    "nombre": "Zabdy",
    "apellido": "Noguez",
    "puesto": "Informática",
    "sueldo": 12000
}
#key toma el valor de una tupla, con su indice y el valor
for key in dicionario.items():
    print(key)
    
#recorremos el valor del diccionario con items() para obtener clave y valor
for datos in dicionario.items():
    key = datos[0]
    valor = datos[1]
    print(f'El indice es: {key} y el valor es: {valor}')
    