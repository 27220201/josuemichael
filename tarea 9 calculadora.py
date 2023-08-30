"""
2) Calculadora Simple: Crea una calculadora simple que pueda realizar operaciones básicas como suma,
resta, multiplicación y división. La calculadora debe aceptar dos números del usuario y el tipo de
operación que desea realizar. Maneja excepciones en caso de errores de entrada.
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("No se puede dividir entre cero")

def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        if operacion == '+':
            resultado = suma(num1, num2)
        elif operacion == '-':
            resultado = resta(num1, num2)
        elif operacion == '*':
            resultado = multiplicacion(num1, num2)
        elif operacion == '/':
            resultado = division(num1, num2)
        else:
            print("Operación no válida. Debe ser '+', '-', '*', o '/'.")
            return

        print("El resultado es: ", resultado)

    except ValueError:
        print("Entrada incorrecta. Asegúrate de ingresar números válidos.")

    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()
