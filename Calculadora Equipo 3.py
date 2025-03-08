#Creado por Rodrigo Rodriguez
def suma(a,b):
    return a+b

#Creada por Luis Enrique
def division(a, b):
    if b == 0:
        return "Error: Division por cero"
        return a / b

#Creada por Brenda
def multiplicacion(a, b):
    return a * b


if __name__ == "__main__":
    print("Selecciona una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    
    operacion = input("Ingresa el nÃºmero de la operacion: ")
    
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