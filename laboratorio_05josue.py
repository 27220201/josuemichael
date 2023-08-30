# TAREA 1
# La siguiente es una lista de las edades de 10 estudiantes:
# edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] (4ptos)
# a. Ordena la lista y encuentra la edad mínima y máxima
# b. Añade de nuevo la edad mínima y máxima a la lista
# c. Encuentra la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)
# d. Encuentra la edad promedio (suma de todos los elementos divididos por su número)
# e. Encuentra el rango de las edades (máximo menos mínimo)
# f. Compara el valor de (mínimo - promedio) y (máximo - promedio), usa el método abs()

# a.
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Lista_ordenada_edades = sorted(edades)
Edad_minima = Lista_ordenada_edades[0]
Edad_maxima = Lista_ordenada_edades[-1]

print("Lista de edades ordenadas son: ", Lista_ordenada_edades)
print("Edad Minima: ", Edad_minima)
print("Edad Maxima: ", Edad_maxima)

# b.
edades.extend([Edad_minima, Edad_maxima])
print("Lista nueva con edades añadidas son: ", edades)

# c.
Lista_ordenada_edades = sorted(edades)
n = len(Lista_ordenada_edades)
if n % 2 == 0:
    Edad_mediana = (Lista_ordenada_edades[n // 2 - 1] + Lista_ordenada_edades[n // 2]) / 2
else:
    Edad_mediana = Lista_ordenada_edades[n // 2]
    
print("Edad Madiana: ", Edad_mediana)
    
# d.
Edad_promedio = sum(edades) / len(edades)
print("El promedio es: ", Edad_promedio)

# e. 
El_rango_de_edades_es = Edad_maxima - Edad_minima
print("El rango es: ", El_rango_de_edades_es)

# f.
Minimo = abs(Edad_minima - Edad_promedio)
Maximo = abs(Edad_maxima - Edad_promedio)

print("Valor de la diferencia n1 es: ", Minimo)
print("Valor de la diferencia n2 es: ", Maximo)


## TAREA 2
# “Soy profesor y me encanta inspirar y enseñar a la gente”. ¿Cuántas palabras únicas se han utilizado en la 
# frase? Usa los métodos de split y sets para obtener las palabras únicas. (4pto)

frase = "Soy profesor y me encanta inspirar y enseñar a la gente"
Palabra = frase.split()
palabras_unicas_son = set(Palabra)

cantidad_palab_unicas = len(palabras_unicas_son)

print(frase)
print("Numero de palabras unicas son: ", cantidad_palab_unicas)


## TAREA 3
# Considera tres listas de números enteros, una con números del 1 al 10, otra con números del 5 al 15, y la 
# última con números del 10 al 20. (5ptos)
# a. Convierte las listas en conjuntos.
# b. Encuentra el conjunto de todos los números que están presentes en las tres listas.
# c. Encuentra el conjunto de todos los números que están presentes en al menos una de las listas.
# d. Encuentra el conjunto de todos los números que están presentes en la primera lista, pero no en la última.
# e. Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla.

# a.
Lista_numero_1 = list(range(1, 10))
Lista_numero_2 = list(range(5, 15))
Lista_numero_3 = list(range(10, 20))

Conj_1 = set(Lista_numero_1)
Conj_2 = set(Lista_numero_2)
Conj_3 = set(Lista_numero_3)

print("Conjunto uno es: ", Conj_1)
print("Conjunto dos es: ", Conj_2)
print("Conjunto tres es: ", Conj_3)

# b. 
Conjunto_interseccion = Conj_1.intersection(Conj_2, Conj_3)
print("Los numeros en las tres listas son: ", Conjunto_interseccion)

# c. 
Conj_numeros_almenos_una_lista = Conj_1.union(Conj_2, Conj_3)
print("Los numeros almenos en una lista son: ", Conj_numeros_almenos_una_lista)

# d. 
Numeros_primera_lista = Conj_1.difference(Conj_3)
print("Los numeros de la primera lista son: ", Numeros_primera_lista)

# e.
tupla_n1 = tuple(Conjunto_interseccion)
tupla_n2 = tuple(Conj_numeros_almenos_una_lista)
tupla_n3 = tuple(Numeros_primera_lista)
print(" ")

suma2 = tupla_n2[0] + tupla_n2[-1]
suma3 = tupla_n3[0] + tupla_n3[-1]
print(suma2)
print(suma3)


## TAREA 4 
# Considera dos listas, l1 y l2, que contienen tuplas. Cada tupla consta de una cadena de texto y un número 
# entero. La lista l1 tiene 5 elementos y la lista l2 tiene 3 elementos. (7ptos)
l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)] 
l2 = [("one", 1), ("two", 2), ("six", 6)]

# Tu tarea es:
# a. Crear conjuntos a partir de estas listas, s1 y s2.
s1 = set(l1)
s2 = set(l2)
print("El conjunto s1: ", s1)

# b. Encontrar los elementos que son comunes a s1 y s2 y almacenarlos en un conjunto s3.
s3 = s1.intersection(s2)
print("El conjunto s3: ", s3)

# c. Encontrar los elementos que son únicos para s1 y s2 y almacenarlos en un conjunto s4.
s4 = s1.symmetric_difference(s2)
print("El conjunto s4: ", s4)

# d. Crear una nueva lista l3 que contenga los elementos de s3 y s4 ordenados por el número entero de cada 
# tupla.
l3 = sorted(list(s3.union(s4)), key= lambda y: y[1]) ## En Python, las lambdas son funciones anónimas que puede aceptar varios argumentos y devolver un valor. 
print(l3)