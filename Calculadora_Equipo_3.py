# Creado por Rodrigo Rodriguez
def sumar(a, b):
    """
    Función para sumar dos números.

    Args:
        a: El primer número (puede ser una cadena o un número).
        b: El segundo número (puede ser una cadena o un número).

    Returns:
        La suma de a y b como un número decimal (float).
        Si la entrada no es válida, devuelve un mensaje de error.
    """
    try:
        a = float(a)  # Intenta convertir a a un número decimal
        b = float(b)  # Intenta convertir b a un número decimal
        return float(a + b)  # Realiza la suma y asegura que el resultado sea decimal
    except ValueError:
        return "Error: Entrada inválida"  # Devuelve un mensaje de error si la entrada no es un número válido

# Creada por Luis Enrique
def dividir(a, b):
    """
    Función para dividir dos números.

    Args:
        a: El dividendo (el número que se va a dividir).
        b: El divisor (el número por el que se va a dividir).

    Returns:
        El resultado de la división de a entre b como un número decimal.
        Si b es cero, devuelve un mensaje de error.
        Si la entrada no es válida, devuelve un mensaje de error.
    """
    try:
        a = float(a)  # Intenta convertir a a un número decimal
        b = float(b)  # Intenta convertir b a un número decimal
        if b == 0:
            return "Error: División por cero"  # Devuelve un mensaje de error si el divisor es cero
        return float(a / b)  # Realiza la división y asegura que el resultado sea decimal
    except ValueError:
        return "Error: Entrada inválida"  # Devuelve un mensaje de error si la entrada no es un número válido

# Creada por Brenda
def multiplicar(a, b):
    """
    Función para multiplicar dos números.

    Args:
        a: El primer número.
        b: El segundo número.

    Returns:
        El producto de a y b como un número decimal.
        Si la entrada no es válida, devuelve un mensaje de error.
    """
    try:
        a = float(a)  # Intenta convertir a a un número decimal
        b = float(b)  # Intenta convertir b a un número decimal
        return float(a * b)  # Realiza la multiplicación y asegura que el resultado sea decimal
    except ValueError:
        return "Error: Entrada inválida"  # Devuelve un mensaje de error si la entrada no es un número válido

# Creada por (Someone - Adding subtraction)
def restar(a, b):
    """
    Función para restar dos números.

    Args:
        a: El minuendo (el número del que se va a restar).
        b: El sustraendo (el número que se va a restar).

    Returns:
        La diferencia entre a y b como un número decimal.
        Si la entrada no es válida, devuelve un mensaje de error.
    """
    try:
        a = float(a)  # Intenta convertir a a un número decimal
        b = float(b)  # Intenta convertir b a un número decimal
        return float(a - b)  # Realiza la resta y asegura que el resultado sea decimal
    except ValueError:
        return "Error: Entrada inválida"  # Devuelve un mensaje de error si la entrada no es un número válido

def precedencia(operador):
    """
    Función para determinar la precedencia de un operador.

    Args:
        operador: El operador a evaluar.

    Returns:
        Un número que representa la precedencia del operador.
        Mayor número significa mayor precedencia.
    """
    if operador in ('+', '-'):
        return 1  # Suma y resta tienen la misma precedencia (baja)
    elif operador in ('*', '/'):
        return 2  # Multiplicación y división tienen la misma precedencia (alta)
    return 0  # Paréntesis tienen la precedencia más baja

def procesar_operacion(operadores, valores):
    """
    Función para realizar una operación utilizando los operadores y valores disponibles.

    Args:
        operadores: Una lista (pila) de operadores pendientes.
        valores: Una lista (pila) de valores numéricos.

    Returns:
        None si la operación se realizó correctamente.
        Un mensaje de error si ocurre un error (por ejemplo, división por cero).
    """
    operador = operadores.pop()  # Obtiene el último operador de la lista de operadores
    valor2 = valores.pop()  # Obtiene el último valor de la lista de valores
    valor1 = valores.pop()  # Obtiene el penúltimo valor de la lista de valores

    if operador == '+':
        valores.append(sumar(valor1, valor2))  # Suma los dos valores y lo agrega a la lista de valores
    elif operador == '-':
        valores.append(restar(valor1, valor2))  # Resta los dos valores y lo agrega a la lista de valores
    elif operador == '*':
        valores.append(multiplicar(valor1, valor2))  # Multiplica los dos valores y lo agrega a la lista de valores
    elif operador == '/':
        resultado = dividir(valor1, valor2)  # Divide los dos valores
        if isinstance(resultado, str):
            return resultado  # Propaga el error si es una división por cero
        valores.append(resultado)  # Agrega el resultado a la lista de valores
    return None

def calcular(expresion):
    """
    Función principal para calcular el resultado de una expresión matemática.

    Args:
        expresion: La expresión matemática en forma de cadena.

    Returns:
        El resultado de la expresión como un número decimal.
        Si la expresión no es válida, devuelve un mensaje de error.
    """
    valores = []  # Lista para almacenar los valores numéricos
    operadores = []  # Lista para almacenar los operadores
    indice = 0  # Índice para recorrer la expresión

    while indice < len(expresion):
        if expresion[indice].isdigit() or expresion[indice] == '.':  # Si el caracter es un dígito o un punto decimal
            j = indice  # Guarda el índice actual
            while j < len(expresion) and (expresion[j].isdigit() or expresion[j] == '.'):  # Avanza hasta que no sea un dígito o un punto decimal
                j += 1
            valores.append(expresion[indice:j])  # Agrega el número a la lista de valores
            indice = j - 1  # Actualiza el índice para la siguiente iteración

        elif expresion[indice] == '(':  # Si el caracter es un paréntesis de apertura
            operadores.append(expresion[indice])  # Agrega el paréntesis a la lista de operadores

        elif expresion[indice] == ')':  # Si el caracter es un paréntesis de cierre
            while operadores and operadores[-1] != '(':  # Mientras haya operadores y el último operador no sea un paréntesis de apertura
                error = procesar_operacion(operadores, valores)  # Realiza la operación
                if error:
                    return error  # Si hay un error, lo devuelve
            operadores.pop()  # Elimina el paréntesis de apertura

        elif expresion[indice] in ('+', '-', '*', '/'):  # Si el caracter es un operador
            while operadores and precedencia(operadores[-1]) >= precedencia(expresion[indice]):  # Mientras haya operadores y la precedencia del último operador sea mayor o igual que la del operador actual
                error = procesar_operacion(operadores, valores)  # Realiza la operación
                if error:
                    return error  # Si hay un error, lo devuelve
            operadores.append(expresion[indice])  # Agrega el operador a la lista de operadores

        indice += 1  # Avanza al siguiente caracter

    while operadores:  # Mientras haya operadores pendientes
        error = procesar_operacion(operadores, valores)  # Realiza la operación
        if error:
            return error  # Si hay un error, lo devuelve

    if len(valores) == 1:  # Si queda un solo valor en la lista de valores
        return valores[0]  # Devuelve el resultado
    else:
        return "Error: Expresión inválida"  # Si no, devuelve un mensaje de error

if __name__ == "__main__":
    print("Ingresa una expresión (ej. 5+5 * 7 - (3-8)):")
    expresion = input("Expresión: ")
    resultado = calcular(expresion)
    print(f"Resultado: {resultado}")
