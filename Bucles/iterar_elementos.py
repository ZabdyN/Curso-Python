
animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [10, 62, 12, 22]
#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

#recorriendo la lista numeros y multiplicar cada valor por 10    
for numero in numeros:
    resultado = numero*10
    print(resultado)
    
for numero,animal in zip(numeros,animales):
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}')
    
for num in range(5,10):
    print(num)
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    #print(type(num))
    #num se vuelve una tupla
    #print(num)
    #el primer valor que devuelve es el índice y el segundo es el dato almacenado
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')

#forma usada comunmente
for i,num in enumerate(numeros):
    print(f'indice: {i} y valor: {num}')
else:
    print("el bucle termino")
    
#Todo lo anterior sirve para listas y tuplas y conjuntos