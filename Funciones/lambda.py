#funciones lambda son el equivalente a funciones flecha en java
#son funciones que no requieren crear un def o una funcion completa, se establecen a través de pseudocódigo estructurado
#retornan valores automaticamente, no funciona con 
multiplicar_por_dos = lambda x : x*2

numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,18,20]

#funcion que indica si un num es par
def es_par(num):
    if (num%2==0):
        return True
    
#usamos filter con una funcion comun: filter regresa todos los valores True unicamente
num_pares = filter(es_par,numeros)
print(list(num_pares))

#Creando lo mismo pero con Lambda
nones = filter(lambda numero:numero%2==1, numeros)
print(list(nones))