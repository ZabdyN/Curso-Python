#Arrays

#Listas list
lista = ["zabdy", True, 1.5, "hola"]
print(lista[0])

#Tuplas la diferencia con la list es que esta no se puede modificar una vez declarada
tupla = ("zabdy", True, 1.5, "hola")
print(tupla[1])
#tupla[3] = "Maquinola" 
#esto no se puede hacer

#Modificando un valor de la lista
lista[3] = "noguez"
print(lista[3])

#Creando un conjunto (set)
conjunto = {"Zabdy","Noguez",True,2.5}
conjunto = {"noguez","zabdy",False,1.9}
#Los conjuntos se pueden sobre escribir pero completos, no puedes modificar elementos individuales
#Y tampoco puedes acceder a sus valores por índice y no repite valores (permite eliminar duplicados facilmente)
print(conjunto)
#print(conjunto[2])

#Creando un diccionario (dict)
#Se define por Clave : Valor (key : value) y separamos por comas
diccionario = {
    'nombre' : "Zabdy",
    'canal' : "Youtube",
    'boleano' : True,
    'altura' : 1.68,
    'duplicado' : "Zabdy"
}

print(diccionario["altura"] + 6) #puedes ocuparlos como su tipo de dato lo permita



