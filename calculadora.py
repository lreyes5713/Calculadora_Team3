# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: DivisiÃ³n por cero"
    return a / b

def modulo(a, b):
    return a % b


if __name__ == "__main__":
    print("Selecciona una operaciÃ³n:")
    print("1. Suma")
    print("2. Resta")
    print("3. MultiplicaciÃ³n")
    print("4. DivisiÃ³n")
    
    operacion = input("Ingresa el nÃºmero de la operaciÃ³n: ")
    
    num1 = float(input("Ingresa el primer nÃºmero: "))
    num2 = float(input("Ingresa el segundo nÃºmero: "))
    
    if operacion == "1":
        print(f"El resultado es: {suma(num1, num2)}")
    elif operacion == "2":
        print(f"El resultado es: {resta(num1, num2)}")
    elif operacion == "3":
        print(f"El resultado es: {multiplicacion(num1, num2)}")
    elif operacion == "4":
        print(f"El resultado es: {division(num1, num2)}")
    else:
        print("OpciÃ³n no vÃ¡lida")