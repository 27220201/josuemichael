"""
3) Generador de Contraseñas: Crea una función que genere contraseñas aleatorias. La función debe
aceptar parámetros como longitud de la contraseña y si debe incluir letras mayúsculas, minúsculas,
números y caracteres especiales. Utiliza funciones lambda para generar caracteres aleatorios y maneja
excepciones si se proporcionan parámetros inválidos.
"""

import random
import string

def generar_contraseña(longitud, mayusculas, minusculas, numeros, caracteres_especiales):
    opciones = ''

    if mayusculas:
        opciones += string.ascii_uppercase
    if minusculas:
        opciones += string.ascii_lowercase
    if numeros:
        opciones += string.digits
    if caracteres_especiales:
        opciones += string.punctuation

    if not opciones:
        raise ValueError("Debes incluir al menos un tipo de carácter en la contraseña")

    generador = lambda: random.choice(opciones)

    try:
        contraseña = ''.join(generador() for _ in range(longitud))
        return contraseña

    except ValueError:
        raise ValueError("Longitud de contraseña inválida")

def main():
    try:
        longitud = int(input("Longitud de la contraseña: "))
        mayusculas = input("Incluir letras mayúsculas (S/N): ").upper() == 'S'
        minusculas = input("Incluir letras minúsculas (S/N): ").upper() == 'S'
        numeros = input("Incluir números (S/N): ").upper() == 'S'
        caracteres_especiales = input("Incluir caracteres especiales (S/N): ").upper() == 'S'

        contraseña_generada = generar_contraseña(longitud, mayusculas, minusculas, numeros, caracteres_especiales)
        print(f"Contraseña generada: {contraseña_generada}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
