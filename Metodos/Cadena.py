cadena1 = "Hola soy Zabdy"
cadena2 = "Hola amigo"

#dir Devuelve la lista de atributos cálidos del objeto (es una función) 
resultado = dir(cadena1)
print(resultado)

#upper Convierte la cadena a mayuscula (método)
resultado = cadena1.upper()
print(resultado)

#lower Convierte la cadena a minusculas (método)
resultado = cadena1.lower()
print(resultado)

#capitalize Primer letra en mayuscula (método)
resultado = cadena1.capitalize()
print(resultado)

#find Método busca una cadena en otra cadena, si no la encuentra regresa -1
busqueda_find = cadena1.find("a")
print(busqueda_find)

#index Método encuentra la primera aparición del valor especificado, si no hay coincidencias devuelve una excepción
busqueda_find = cadena1.index("Z")
print(busqueda_find)

#isnumeric Si es numerico devuelve True
resultado = cadena1.isnumeric()
print(resultado)

#isalpha Si es alfa numérico devuelve True (el espacio no son alfa numerico, no cuenta caracteres especiales)
resultado = cadena1.isalpha()
print(resultado)

#count Devuelve el numero de ocurrencias en una cadena
resultado = cadena1.count("a")
print(resultado)

#len cuenta cuantos caracteres hay en una cadena
#como método
resultado = cadena1.__len__()
print(resultado)
#como función
resultado = len(cadena1)
print(resultado)

#starswith Se verifica si una cadena empieza con otro cadena dada, devuelve True
resultado = cadena1.startswith("Hola")
print(resultado)

#endswith Se verifica si una cadena termina con otra cadena dada, devuelve True
resultado = cadena1.endswith("dy")
print(resultado)

#replace Reemplaza un pedazo de la cadena dada, por otra cadena dada
cadena_nueva = cadena1.replace("ola", "ello")
print(cadena_nueva)

#split Separa cadenas con la cadena que le pasemos
resultado = cadena1.split(" ")
print(resultado)
