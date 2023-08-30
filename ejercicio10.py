#La siguiente es una lista de las edades de 10 estudiantes:
#edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 
@
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edades.sort() 

edad_minima = edades[0] 
edad_maxima = edades[-1] 

print("La edad mínima es:", edad_minima)
print("La edad máxima es:", edad_maxima)

#Añade de nuevo la edad mínima y máxima a la lista
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edad_minima = min(edades) 
edad_maxima = max(edades) 

edades.append(edad_minima) 
edades.append(edad_maxima) 

print(edades)

#Encuentra la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edades_ordenadas = sorted(edades) 

longitud = len(edades_ordenadas) 

if longitud % 2 == 0:
    indice_medio = longitud // 2
    edad_mediana = (edades_ordenadas[indice_medio - 1] + edades_ordenadas[indice_medio]) / 2
else:
    indice_medio = longitud // 2
    edad_mediana = edades_ordenadas[indice_medio]

print("La edad mediana es:", edad_mediana)

#Encuentra la edad promedio (suma de todos los elementos divididos por su número)
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
promedio = sum(edades) // len(edades)
print("La edad promedio es:", promedio)

#Encuentra el rango de las edades (máximo menos mínimo
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
rango = max(edades) - min(edades)
print("El rango de las edades es:", rango)

#Compara el valor de (mínimo - promedio) y (máximo - promedio), usa el método abs()
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
promedio = sum(edades) / len(edades)
diferencia_min = abs(min(edades) - promedio)
diferencia_max = abs(max(edades) - promedio)

print("La diferencia entre el mínimo y el promedio es:", diferencia_min)
print("La diferencia entre el máximo y el promedio es:", diferencia_max)

