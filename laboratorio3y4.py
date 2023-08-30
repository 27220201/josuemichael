## Tarea 1
# Encuentra la longitud del texto python, convierte el valor a float y luego conviértelo a string (1pto)

palabra = 'python'
print ('Longitud es: ', len(palabra))

print('VAlor en float: ', float(len(palabra)))
print('VAlor en string: ', palabra)

# De otra forma 
texto = "python"
longitud = len (texto)
float_longitud = float(longitud)
str_longitud = str (float_longitud)
print("Longitud del texto pyton es:", longitud)
print("Valor a floar:", float_longitud)
print("Valor a string:", str_longitud)

## Tarea 2
# Escribe un script en Python que muestre la siguiente tabla (1pto)
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')

## Tarea 3
# La siguiente lista contiene los nombres de algunas bibliotecas de python: ['Django', 'Flask', 'Bottle', 
# 'Pyramid', 'Falcon']. Une la lista con una cadena de espacio de hash(#). (1pto)

bibliotecas_de_python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado = '#'.join(bibliotecas_de_python)
print("La nueva lista es: ", resultado)

## Tarea 4
# Usa la secuencia de escape de tabulación para escribir las siguientes líneas. (1pto)
# Nombre Edad País Ciudad
# Edem 250 Perú Ayacucho

Linea1 = 'Nombre\tEdad\tPaís\tCiudad'
Linea2 = 'Edem\t250\tPerú\tAyacucho'
print(Linea1.expandtabs())
print(Linea2.expandtabs())

## Tarea 5
# Usa el método de formato de cadena para mostrar lo siguiente: (1pto)
# radio = 10
# area = 3.14 * radio ** 2
# El área de un círculo con radio 10 es 314 metros cuadrados.

radio = 10
area = 3.14 * radio ** 2
resultado = 'El área de un círculo con radio {} es {} metros cuadrados.'.format(str(radio), str(area))
print(resultado)

## Tarea 6
# Realiza lo siguiente utilizando métodos de formateo de cadenas: (1pto)
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

suma = '8 + 6 = 14'
resta = '8 - 6 = 2'
multiplicacion = '8 * 6 = 48'
division = '8 / 6 = 1.33'
modulo = '8 % 6 = 2'
division_de_piso = '8 // 6 = 1'
Exponenciacion = '8 ** 6 = 262144'
frase = 'La suma de {}, El resultado de la resta de {}. La multiplicacion de {}. La division de {}.'.format(suma, resta, multiplicacion, division)
frase2 = 'El modulo de {}. La division de piso de {}. La exponenciacion de {}.'.format(modulo, division_de_piso, Exponenciacion)
print(frase)
print(frase2)

## Tarea 7
# Contar caracteres y palabras: Dada la siguiente frase: "Estoy aprendiendo Python y me está 
# gustando mucho. ¡Es genial!". Escribe un programa en Python que cuente el número de palabras y de 
# caracteres (incluyendo espacios y signos de puntuación). (3pto)

frase = "Estoy aprendiendo Python y me está gustando mucho. ¡Es genial!"

Num_palabras = frase.split()
numero_de_palabras = len(Num_palabras)

numero_de_caracteres = len(frase)

print("Número de caracteres:", numero_de_caracteres)
print("Número de palabras:" , numero_de_palabras)

## Tarea 8
# Inversión de palabras en una frase: Dada la frase "Aprendiendo Python con Edem". Escribe un 
# programa que invierta el orden de las palabras en la frase, pero mantenga el orden de los caracteres en cada 
# palabra. El resultado debería ser: "Edem con Python Aprendiendo".(3pto)

frase = "Aprendiendo Python con Edem"
palabras = frase.split()
frase_invertido = " ".join(reversed(palabras))
print(frase_invertido)

## Tarea 9
# Cifrado César: El cifrado César es una técnica de cifrado simple en la que cada letra en el texto original se 
# reemplaza por una letra un cierto número de posiciones más adelante en el alfabeto. Por ejemplo, con un 
# desplazamiento de 1, "A" se reemplazaría por "B", "B" se convertiría en "C", etc. Escribe un programa que 
# implemente el cifrado César para un mensaje y un desplazamiento dados. (5pto)

mensaje = input("Ingrese mensaje: ").upper()
n_desplazamiento = int(input("Ingrese desplazamiento: "))

abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

cifrado = " "

for k in mensaje: 
    if k in abc: 
        pos_letra = abc.index(k)
        nueva_pos = (pos_letra + n_desplazamiento) % len(abc)
        cifrado += abc[nueva_pos]
    else: 
        cifrado+=k

print("Mensaje Cifrado Cesar: ", cifrado)

## Tarea 10 
# Palíndromos: Un palíndromo es una palabra, frase, número u otro tipo de unidad que se puede leer igual 
# hacia adelante que hacia atrás (ignorando espacios, acentos y signos de puntuación), como "anilina" o 
# "reconocer". Escribe un programa en Python que detecte si una frase dada es un palíndromo. (3pto)

frase = input('Ingrese frase: ')
if str(frase) == str(frase) [::-1]:
    print('Es palíndromo')
else:
    print('No es palíndromo')