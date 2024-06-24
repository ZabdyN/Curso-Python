diccionario = {
    "nombre" : "Zabdy",
    "apellido" : "Noguez",
    "años" : 38
}

#keys nos muestra las claves (nombres) de nuestros elementos en el diccionario
#tambien sirve para iterar los keys
claves = diccionario.keys()
print(claves)

#get devuelve el valor de una clave
claves = diccionario.get("apellido")
#claves = diccionario["apellido"] esto devuelve una excepción si no encuentra la clave, mientras que get omite dicha excepción
print(claves)

#pop elimina un elemento del diccionario
diccionario.pop("años")
print(diccionario)

#clear elimina todo el diccionario
diccionario.clear()
print(diccionario)