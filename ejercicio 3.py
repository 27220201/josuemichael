#Considera tres listas de números enteros, una con números del 1 al 10, otra con números del 5 al 15, y la
#última con números del 10 al 20.
#a. Convierte las listas en conjuntos.
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

print(conjunto1)
print(conjunto2)
print(conjunto3)

#b. Encuentra el conjunto de todos los números que están presentes en las tres listas.
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

resultado = conjunto1.intersection(conjunto2, conjunto3)

print(resultado)

#Encuentra el conjunto de todos los números que están presentes en al menos una de las listas
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

resultado = conjunto1.union(conjunto2, conjunto3)

print(resultado)

#Encuentra el conjunto de todos los números que están presentes en la primera lista, pero no en la última
lista1 = list(range(1, 11))
lista3 = list(range(10, 21))

conjunto1 = set(lista1)
conjunto3 = set(lista3)

resultado = conjunto1.difference(conjunto3)

print(resultado)
#Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla.
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

tupla1 = tuple(conjunto1)
tupla2 = tuple(conjunto2)
tupla3 = tuple(conjunto3)

suma1 = tupla1[0] + tupla1[-1]
suma2 = tupla2[0] + tupla2[-1]
suma3 = tupla3[0] + tupla3[-1]

print(suma1, suma2, suma3)