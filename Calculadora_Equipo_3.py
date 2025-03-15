# Creado por Rodrigo Rodriguez
def suma(a, b):
    try:
        a = float(a)
        b = float(b)
        return float(a + b)  # Verifica resultado decimal
    except ValueError:
        return "Error: Numeros invalidos"

# Creada por Luis Enrique
def division(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            return "Error: Division por cero"
        return float(a / b)  # Verifica resultado decimal
    except ValueError:
        return "Error: Numeros invalidos"

# Creada por Brenda
def multiplicacion(a, b):
    try:
        a = float(a)
        b = float(b)
        return float(a * b)  # Verifica resultado decimal
    except ValueError:
        return "Error: Invalid input"


def resta (a, b):
    try:
        a = float(a)
        b = float(b)
        return float(a - b)  # Verifica resultado decimal
    except ValueError:
        return "Error: Invalid input"


def calculo (expresion):
    operadores_permitidos = ['+', '-', '*', '/']
    num1 = ''
    num2 = ''
    op = ''

    for char in expresion:
        if char.isdigit() or char == '.':
            if not op:
                    num1 += char
            else:
                num2 += char
        elif char in operadores_permitidos:
            if not op:
                    op = char
            else:
                return "Expresion invalida, demasiados operadores"
        elif char == ' ':
            continue
        else:
            return "Error caracteres invalidos"

    if not num1 or not num2 or not op:
        return "Expresion incompleta"
                
    if op == '+':
        return suma (num1, num2)
    elif op == '-':
        return resta (num1, num2)
    elif op == '*':
        return multiplicacion (num1, num2)
    elif op == '/':
        return division (num1, num2)
    else:    
        return "Operacion invalida"

'''
if __name__ == "__main__":
    print("Selecciona una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    
    operacion = input("Ingresa el numero de la operacion: ")
    
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))
    
    if operacion == "1":
        print(f"El resultado es: {suma(num1, num2)}")
    elif operacion == "2":
        print(f"El resultado es: {resta(num1, num2)}")
    elif operacion == "3":
        print(f"El resultado es: {multiplicacion(num1, num2)}")
    elif operacion == "4":
        print(f"El resultado es: {division(num1, num2)}")
    else:
        print("Opcion no valida")

'''

if __name__ == "__main__":
    print("Ingresa tu operacion (ejemplo, 2 + 3.5):")
    expresion = input("Expresion: ")
    resultado = calculo(expresion)
    print(f"Resultado: {resultado}")