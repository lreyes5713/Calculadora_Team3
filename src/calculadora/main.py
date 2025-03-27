from src.calculadora.calcular_expresion import calcular


if __name__ == "__main__":
    # Interfaz del programa
    print("Calculadora matemática")
    print("Operadores permitidos: +, -, *, /, ^, sqrt")
    print("Ejemplo: 5 + (8*9) - 5.5^2 + sqrt(8)")

    while True:
        expresion = input("\nIngrese la expresión (o 'salir' para terminar): ")  # Solicita la expresión al usuario
        if expresion.lower() == 'salir':
            break  # Termina el programa si el usuario escribe 'salir'
        resultado = calcular(expresion)
        if isinstance(resultado, str):
            print(f"Error: {resultado}")  # Muestra mensaje de error si lo hay
        else:
            print(f"Resultado: {resultado:.8f}")  # Muestra el resultado con 8 decimales
