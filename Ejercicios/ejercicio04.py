#ejercicio para devolver los numeros primos que hay entre 0 y X cantidad

def es_primo(num):
    #range permite evaluar un intervalo en este caso desde 2 hasta num-1
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(2,num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(33)
print(resultado)