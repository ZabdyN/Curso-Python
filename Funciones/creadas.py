# #creando una funcion simple
# def saludar():
#     print("hola Zabdy")
    
# saludar()

#Creando una función con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
    
    print(f"Hola {nombre} mi {adjetivo} ¿Cómo estás?")
    
saludar("Zabdy","no binario")
saludar("Fran","Mujer")
saludar("Carlos","HOMBRE")

#Creando una función que nos retorne multiples valores
def calculo(num):
    chars = "wekjdfgsdgls"
    
    numero = str(num)
    num = int(numero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contra = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contra,num
    
password = calculo(3)
frase = f"Tu contraseña nueva es: {password}"
print(frase)

#desempaquetando la funcion
password, primer_num = calculo(984)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contaseña nueva es: {password}")
print(f"El num utilizado para crearla fue: {primer_num}")


    


