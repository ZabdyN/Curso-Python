#creando diccionario con dict()

diccionario = dict(nombre="Zabdy", apellido="Noguez")

#sólo se pueden crear objetos vacion con sus respectivos "funciones" dict, list, tuple
print(diccionario)

#las listas no pueden ser claves porque son mutables
diccionario = {("dalto", "lols"): "el jajas"}
print(diccionario)

#Las listas no pueden ser  claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "apelli"]): "el jojos"}
print(diccionario)

#creando diccionarios con fromkeys
diccionario = dict.fromkeys("ABCDEFG","skdhfksjdf") #el primer dato es un iterable, regularmente se usa para hacer una lista de keys vacia
print(diccionario)
#Se puede pasar el valor como lista y el valor por defecto es None
diccionario = dict.fromkeys(["Nombre", "Apellido", "ciudad"])
print(diccionario)

diccionario = dict.fromkeys("ZXYFC")
print(diccionario)

