import pytest
from src.calculadora.calcular_expresion import calcular


@pytest.mark.parametrize("expresion", [("abc")])
def test_calcular_entrada_invalida(expresion):
    assert calcular(expresion) == "Error: Expresión inválida"


@pytest.mark.parametrize("expresion", [("2 +"), ("+ 3 + 4")])
def test_calcular_operandos_faltantes(expresion):
    assert calcular(expresion) == "Error: Faltan operandos"


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
