from src.calculadora.calcular_expresion import calcular


if __name__ == "__main__":
    print("Ingresa una expresión (ej. 5+5 * 7 - (3-8)^2):")
    expresion = input("Expresión: ")
    resultado = calcular(expresion)
    print(f"Resultado: {resultado}")
