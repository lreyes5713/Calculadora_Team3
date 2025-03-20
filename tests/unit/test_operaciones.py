import pytest
from src.calculadora.operaciones import sumar, restar, multiplicar, dividir, potenciar

test_inputs = {"sumas": [(2, 3, 5.0), (-1, 1, 0.0), (2.5, 3.5, 6.0), ("2", "3", 5.0)],
               "restas": [(5, 2, 3.0), (1, -1, 2.0), (5.5, 2.5, 3.0), ("5", "2", 3.0)],
               "multis": [(2, 3, 6.0), (-1, 5, -5.0), (2.5, 2, 5.0), ("2", "3", 6.0)],
               "divis": [(6, 2, 3.0), (5, -2, -2.5), (2.5, 0.5, 5.0), ("6", "2", 3.0), (5, 0, "Error: División por cero")],
               "pots": [(3, 2, 9.0), (2, -2, 0.25), (-2.5, 2, 6.25), ("4", "3", 64.0)]
               }


@pytest.mark.parametrize("num1, num2, sum", test_inputs["sumas"])
def test_sumar(num1, num2, sum):
    assert sumar(num1, num2) == sum


@pytest.mark.parametrize("num1, num2, res", test_inputs["restas"])
def test_restar(num1, num2, res):
    assert restar(num1, num2) == res


@pytest.mark.parametrize("num1, num2, mul", test_inputs["multis"])
def test_multiplicar(num1, num2, mul):
    assert multiplicar(num1, num2) == mul


@pytest.mark.parametrize("num1, num2, div", test_inputs["divis"])
def test_dividir(num1, num2, div):
    assert dividir(num1, num2) == div

@pytest.mark.parametrize("num1, num2, pot", test_inputs["pots"])
def test_potenciar(num1, num2, pot):
    assert potenciar(num1, num2) == pot
