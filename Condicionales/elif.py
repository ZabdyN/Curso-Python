ingrso_mensual = 81000
gasto_mensual = 80000

#If anidados y else if (elif)
if ingrso_mensual > 10000:
    print("Estás bien en cualquier parte del mundo")
    if ingrso_mensual - gasto_mensual < 0:
        print("Estás en déficit")
    elif ingrso_mensual - gasto_mensual > 3000:
        print("Estás bien!")
    else:
        print("Estás gastando más de lo que ganas")
    
elif ingrso_mensual > 1000:
    print("Estás bien en latinoamerica")
    
elif ingrso_mensual > 500:
    print("Estás bien en Argentina")
    
elif ingrso_mensual > 200:
    print("Estás bien en Venezuela")
    
else:
    print("Eres pobre")
    
