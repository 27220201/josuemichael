"""
3) Ejercicio Complejo: Generador de Contraseñas Seguras
Descripción: Vamos a crear un generador de contraseñas seguras utilizando los conceptos que hemos 
aprendido hasta ahora, incluyendo funciones, módulos y control de flujo. La idea es que el programa genere 
una contraseña aleatoria con una longitud específica y asegure que cumple con ciertos requisitos de 
seguridad.
a) Requisitos de seguridad de la contraseña:
b) La contraseña debe tener al menos 8 caracteres.
c) Debe incluir al menos una letra mayúscula y una letra minúscula.
d) Debe contener al menos un número.
e) Debe contener al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.)
"""

import random
import string

def generador_contraseña(longitud):
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    digitos = string.digits
    caracteres_especiales = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    if longitud < 8:
        print("La longitud mínima de la contraseña es 8 caracteres.")
        return

    while True:
        contraseña = random.choice(letras_minusculas) + random.choice(letras_mayusculas) + random.choice(digitos) + random.choice(caracteres_especiales) + \
                     ''.join(random.choice(letras_minusculas + letras_mayusculas + digitos + caracteres_especiales) for _ in range(longitud-4))

        contraseña = ''.join(random.sample(contraseña, len(contraseña)))

        if (any(i in letras_minusculas for i in contraseña) and
            any(i in letras_mayusculas for i in contraseña) and
            any(i in digitos for i in contraseña) and
            any(i in caracteres_especiales for i in contraseña)):
            return contraseña

longitud_de_contraseña = int(input("Ingresa la longitud deseada para la contraseña: "))
contraseña = generador_contraseña(longitud_de_contraseña)
print("Contraseña generada:", contraseña)
