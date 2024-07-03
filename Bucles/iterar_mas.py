frutas = ["platano", "manzana", "pera", "ciruela", "granada", "durazno"]
cadena = "Hola Zabdy"
numeros = [2, 4, 5, 8, 15]
#evitando que un elemento usando continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Me voy a comer una: {fruta}")
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco despues de un break)
for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")
    if fruta == "pera":
        break
else:
    print("Terminado")
    
#Iterando una cadena caracter por caracter    
for letra in cadena:
    print(letra)
    
#For crear una lista con el valor de cada numero de numeros al doble
numeros_2 = list()
for numero in numeros:
    numeros_2.append(numero*2)
    
print(numeros_2)

#asi se hace en una sola linea
numeros_2 = [x*2 for x in numeros]
print(numeros_2)
