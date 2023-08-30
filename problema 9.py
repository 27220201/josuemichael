mensaje = input("Introduce el mensaje a cifrar: ")
desplazamiento = int(input("Introduce el desplazamiento: "))

mensaje_cifrado = ""

for letra in mensaje:
    if letra.isalpha():
        letra_cifrada = chr((ord(letra) - 65 + desplazamiento) % 26 + 65)
    else:
        letra_cifrada = letra
    mensaje_cifrado += letra_cifrada

print("El mensaje cifrado es:", mensaje_cifrado)
