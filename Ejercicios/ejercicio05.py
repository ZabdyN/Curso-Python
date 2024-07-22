#Serie de Fibonacci

def fibonacci (num):
    a, b = 0, 1
    fibo_list = [0]
    for i in range(num):
        if b > num: return fibo_list
        else: 
            fibo_list.append(b)
            a,b = b,a+b
            
resultado = fibonacci(54)
print(resultado)
        