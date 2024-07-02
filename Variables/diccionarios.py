#creando diccionario con dict()

diccionario = dict(nombre="Zabdy", apellido="Noguez")

#sólo se pueden crear objetos vacion con sus respectivos "funciones" dict, list, tuple
print(diccionario)

#las listas no pueden ser claves porque son mutables
diccionario = {("dalto", "lols"): "el jajas"}
print(diccionario)



diccionario = {frozenset(["dalto", "apelli"]): "el jojos"}
print(diccionario)

