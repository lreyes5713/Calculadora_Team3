import pytest
from Calculadora_Equipo_3 import sumar, restar, multiplicar, dividir, calcular


def test_sumar():
    assert sumar(2, 3) == 5.0
    assert sumar(-1, 1) == 0.0
    assert sumar(2.5, 3.5) == 6.0
    assert sumar("2", "3") == 5.0


def test_restar():
    assert restar(5, 2) == 3.0
    assert restar(1, -1) == 2.0
    assert restar(5.5, 2.5) == 3.0
    assert restar("5", "2") == 3.0


def test_multiplicar():
    assert multiplicar(2, 3) == 6.0
    assert multiplicar(-1, 5) == -5.0
    assert multiplicar(2.5, 2) == 5.0
    assert multiplicar("2", "3") == 6.0


def test_dividir():
    assert dividir(6, 2) == 3.0
    assert dividir(5, -2) == -2.5
    assert dividir(2.5, 0.5) == 5.0
    assert dividir("6", "2") == 3.0
    assert dividir(5, 0) == "Error: División por cero"


def test_calcular_entrada_invalida():
    assert calcular("abc") == "Error: Expresión inválida"
    assert calcular("2 +") == "Error: Expresión inválida"
    assert calcular("+ 3 + 4") == "Error: Expresión inválida"


def test_integracion_expresion1():
    expresion = "(5+5)*(1.25-0.75)"
    # Evaluar manualmente la expresión usando la función calcular
    valor1_op = calcular("5+5")
    valor2_op = calcular("1.25-0.75")
    # Si la función calcular devuelve mensajes de error en cadena, manejarlos aquí
    if isinstance(valor1_op, str) or isinstance(valor2_op, str):
        pytest.fail(f"Error en sub-expresión: valor1_op={valor1_op}, valor2_op={valor2_op}")
    resultado_esperado = float(valor1_op) * float(valor2_op)
    assert calcular(expresion) == resultado_esperado
    assert calcular(expresion) == 5.0


def test_integracion_expresion2():
    expresion = "(8+7/5)*(15-3/8)"
    # Evaluar manualmente la expresión usando la función calcular
    valor1_op = calcular("8+7/5")
    valor2_op = calcular("15-3/8")
    # Si la función calcular devuelve mensajes de error en cadena, manejarlos aquí
    if isinstance(valor1_op, str) or isinstance(valor2_op, str):
        pytest.fail(f"Error en sub-expresión: valor1_op={valor1_op}, valor2_op={valor2_op}")
    resultado_esperado = float(valor1_op) * float(valor2_op)
    assert calcular(expresion) == resultado_esperado
    assert calcular(expresion) == 137.475
