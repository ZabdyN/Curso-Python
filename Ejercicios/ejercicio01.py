#Ejercicio 1.1 Diferencia en porcentaje entre el curso actual y
#el más rápido de los otros cursos

este_curso = 1.5
otro_rapido = 2.5
otro_lento = 7
promedio = 4

print(f"La duración del curso actual fue de {este_curso} horas y la duración del curso más rápido fue de {otro_rapido} horas por lo que: es {100-(este_curso*100/otro_rapido)}% más rapido este curso")

#el más lento de los otros cursos
print(f"La duración del curso actual fue de {este_curso} horas y la duración del curso más lento fue de {otro_lento} horas por lo que: es {100-(este_curso*1000//otro_lento/10)}% más rapido este curso")

#el promedio de los cursos
print(f"La duración del curso actual fue de {este_curso} horas y la duración promedio de los otros fue de {promedio} horas por lo que: es {100-(este_curso*100/promedio)}% más rapido este curso")

#Porcentaje de material inservible
#el promedio de los otros cursos

crudo_curso = 3.5
crudo_otro = 5

print(f"\nSe redujo un {100-(promedio*100/crudo_otro)}% de material inservible en promedio de los otros cursos")

print(f"Se redujo un {100-(este_curso*1000//crudo_curso/10)}% de material inservible de este curso")

#A cuanto equivalen ver 10 de este curso con respecto al promedio de otros cursos

print(f"\nVer 10 horas de este curso equivalen a {100*promedio//este_curso/10} horas del promedio otros cursos")
print(f"Ver 10 horas de este curso equivalen a {100*otro_rapido//este_curso/10} horas del mas rapido de otros cursos")
print(f"Ver 10 horas de este curso equivalen a {100*otro_lento//este_curso/10} horas del mas lento de otros cursos")

print(f"\nVer 10 horas de otros cursos en promedio equivalen a ver {100*este_curso//promedio/10} horas de este curso")
print(f"Ver 10 horas del mas rapido de otros cursos equivalen a ver {10*este_curso/otro_rapido} horas de este curso")
print(f"Ver 10 horas del mas lento de otros cursos equivalen a ver {100*este_curso//otro_lento/10} horas de este curso")