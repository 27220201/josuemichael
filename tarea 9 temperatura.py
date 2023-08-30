"""
1) Conversor de Temperatura: Escribe un programa que convierta entre Celsius y Fahrenheit. El
programa debe permitir al usuario ingresar una temperatura y la unidad en la que está (C o F). Luego,
realiza la conversión y muestra el resultado. Utiliza funciones y control de flujo para realizar las
conversiones y manejar excepciones en caso de entradas incorrectas.
"""

def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        temperatura = float(input("Ingrese la temperatura: "))
        unidad = input("Ingrese la unidad de temperatura (C o F): ").upper()

        if unidad == 'C':
            temperatura_convertida = celsius_a_fahrenheit(temperatura)
            unidad_convertida = 'Fahrenheit'
        elif unidad == 'F':
            temperatura_convertida = fahrenheit_a_celsius(temperatura)
            unidad_convertida = 'Celsius'
        else:
            print("Unidad no válida. Debe ser 'C' o 'F'.")
            return

        print(f"La temperatura convertida es: {temperatura_convertida:.2f} {unidad_convertida}")

    except:
        print("Entrada incorrecta. Asegúrate de ingresar un número válido.")

if __name__ == "__main__":
    main()
