#Crear una lista con list (poco usado)
lista = list(["Hola", "Zabdy", 34])
print(lista)

#Contar los elementos de la lista
cadena = len(lista)
print(cadena)

#Agregar elementos a una lista
#Append agrega un elemento al final de la lista
lista.append("Append")
#modifica directamente a la lista
print(lista)

#insert agrega un elemento a la lista en un indice definido
lista.insert(2, "Insert")
print(lista)

#extend agrega varios elementos al final de la lista por medio de otra lista
lista.extend([False, 2030])
print(lista)

#pop elimina un elemento de la lista por su indice
lista.pop(0)
#lista.pop(-1) para eliminar el último elemento de la lista, -2 para el penúltimo elemeno y así sucesivamente
print(lista)

#remove elimina un elemento de vista por su valor
lista.remove(False)
print(lista)

#clear elimina todos los elementos de una lista
lista.clear()
print(lista)


lista = [68, 13, 85, True, False, 123, 12]
#reverse cambia el orden de la lista, del último al primero
lista.reverse()
print(lista)
#sort ordena elementos en una lista False>True>Numeros (no ordena strings)
lista.sort()
print(lista)
#para ordenar a la invers usamos reverse
lista.sort(reverse=True)
print(lista)

#index busca un elemento en la lista y retorna su indice
elemento_encontrado = lista.index(13)
#busca elementos completos y no una parte
print(elemento_encontrado)


