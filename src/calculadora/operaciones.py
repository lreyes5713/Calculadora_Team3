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


def potenciar(a, b):
    """
    Función para realizar potencia de un numero.

    Args:
        a: El numero base.
        b: El exponente.

    Returns:
        El valor a elevado al valor b.
        Si la entrada no es válida, devuelve un mensaje de error.
    """
    try:
        a = float(a)
        b = float(b)
        return float(a**b)
    except ValueError:
        return "Error: Entrada inválida"
    
    # Raíz cuadrada

    """
    Función para calcular la raíz cuadrada de un número.

    Args:
        numero: El número del que se desea calcular la raíz cuadrada.

    Returns:
        La raíz cuadrada de 'numero' como un número decimal.
        Si la entrada no es válida o negativa, devuelve un mensaje de error.
    """

    def raiz_cuadrada(numero):
        if numero < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo."
        else:
            return numero ** 0.5

