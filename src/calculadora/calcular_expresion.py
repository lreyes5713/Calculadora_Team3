from src.calculadora.operaciones import sumar, restar, multiplicar, dividir, potenciar, raiz_cuadrada


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
    elif operador == ('^'):
        return 3  # Mayor precedencia para potencia
    elif operador == 'sqrt':
        return 4   # Máxima precedencia para raíz cuadrada
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
    if operador == 'sqrt':  # Raíz cuadrada solo necesita un valor
        if not valores:
            return "Error : Falta numero para sqrt"
        valor = valores.pop()
        resultado = raiz_cuadrada(valor)
        if isinstance(resultado, str):  # Si el resultado es un mensaje de error
            return resultado  # Retorna el mensaje de error
        valores.append(resultado)  # Añade el resultado a la lista de valores

    else:  # Si el operador es binario (necesita dos valores +,-,*,/,^)
        valor2 = valores.pop()  # Obtiene el último valor
        valor1 = valores.pop()  # Obtiene el penúltimo valor
        if operador == '+':  # Si el operador es suma
            valores.append(sumar(valor1, valor2))  # Realiza suma y agrega resultado
        elif operador == '-':  # Si el operador es resta
            valores.append(restar(valor1, valor2))  # Realiza resta y agrega resultado
        elif operador == '*':  # Si el operador es multiplicación
            valores.append(multiplicar(valor1, valor2))  # Realiza multiplicación y agrega resultado
        elif operador == '/':  # Si el operador es división
            resultado = dividir(valor1, valor2)  # Divide los valores
            if isinstance(resultado, str):
                return resultado  # Propaga el error si lo hay
            valores.append(resultado)  # Agrega resultado
        elif operador == '^':  # Si el operador es potencia
            valores.append(potenciar(valor1, valor2))  # Realiza potencia y agrega resultado
    return None  # Retorna None si todo salió bien


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
    bandera = False  # Bandera para detectar operadores consecutivos

    while indice < len(expresion):
        if expresion[indice].isdigit() or expresion[indice] == '.':  # Si el caracter es un dígito o un punto decimal
            j = indice  # Guarda el índice actual
            while j < len(expresion) and (expresion[j].isdigit() or expresion[j] == '.'):  # Avanza hasta que no sea un dígito o un punto decimal
                j += 1
            valores.append(expresion[indice:j])  # Agrega el número a la lista de valores
            indice = j - 1  # Actualiza el índice para la siguiente iteración
            bandera = False

        elif expresion[indice] == '(':  # Si el caracter es un paréntesis de apertura
            operadores.append(expresion[indice])  # Agrega el paréntesis a la lista de operadores
            bandera = False

        elif expresion[indice] == ')':  # Si el caracter es un paréntesis de cierre
            while operadores and operadores[-1] != '(':  # Mientras haya operadores y el último operador no sea un paréntesis de apertura
                error = procesar_operacion(operadores, valores)  # Realiza la operación
                if error:
                    return error  # Si hay un error, lo devuelve
            if not operadores:
                return "Error: Paréntesis no balanceados"  # Verifica que haya un '(' correspondiente
            operadores.pop()  # Elimina el paréntesis de apertura
            bandera = False

        elif expresion[indice] in ('+', '-', '*', '/', '^'):  # Si encuentra un operador
            if bandera:
                return "Error: Operadores consecutivos no permitidos"  # Retorna error por operadores consecutivos
            # Resuelve operadores de mayor o igual precedencia antes de agregar el nuevo
            while (operadores and operadores[-1] != '(' and 
                   precedencia(operadores[-1]) >= precedencia(expresion[indice])):  # Mientras haya operadores con mayor o igual precedencia
                error = procesar_operacion(operadores, valores)  # Procesa la operación
                if error:  # Si hay un error
                    return error  # Retorna el error
            operadores.append(expresion[indice])  # Añade el operador a la lista
            bandera = True

        elif expresion[indice:indice+4] == 'sqrt':  # Si encuentra "sqrt"
            operadores.append('sqrt')  # Añade "sqrt" a la lista de operadores
            indice += 3   # Avanza el índice más allá de "sqrt"
            bandera = True

        indice += 1  # Incrementa el índice

    while operadores:  # Mientras haya operadores pendientes
        if operadores[-1] == '(':
            return "Error: Paréntesis no balanceados"  # Verifica paréntesis sobrantes
        error = procesar_operacion(operadores, valores)  # Procesa la operación
        if error:  # Si hay un error
            return error  # Retorna el error

    if len(valores) != 1:
        return "Error: Expresión inválida"  # Verifica que quede solo un resultado
    try:
        return float(valores[0])  # Convierte el resultado final a float
    except ValueError:
        return "Error: Resultado inválido"  # Retorna error si el resultado no es válido
