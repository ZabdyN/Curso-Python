#creando un conjunto con set
conjunto = set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dat2"])
conjunto2 = {conjunto1, "dato3"}


print(conjunto)

print(conjunto2)

#teoria de conjntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
#subconjunto
resultado = conjunto2.issubset(conjunto1)
print(resultado)
#issubset es igual a "<="
resultado = conjunto2 <= conjunto1
print(resultado)
#superconjunto
resultado = conjunto1.issuperset(conjunto2)
print(resultado)

resultado = conjunto1 > conjunto2
print(resultado)
#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)
#solo será True cuando los conjuntos comparados no tengan ningún elemento que coincida




