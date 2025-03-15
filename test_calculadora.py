import pytest
from Calculadora_Equipo_3 import suma, resta, multiplicacion, division, calculo

def test_suma():
    assert suma(2, 3) == 5.0
    assert suma(-1, 1) == 0.0
    assert suma(2.5, 3.5) == 6.0
    assert suma("2", "3") == 5.0

def test_resta():
    assert resta(5, 2) == 3.0
    assert resta(1, -1) == 2.0
    assert resta(5.5, 2.5) == 3.0
    assert resta("5", "2") == 3.0

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6.0
    assert multiplicacion(-1, 5) == -5.0
    assert multiplicacion(2.5, 2) == 5.0
    assert multiplicacion("2", "3") == 6.0

def test_division():
    assert division(6, 2) == 3.0
    assert division(5, -2) == -2.5
    assert division(2.5, 0.5) == 5.0
    assert division("6", "2") == 3.0
    assert division(5, 0) == "Error: Division por cero"

def test_calculate_invalid_input():
    assert calculo("abc") == "Error caracteres invalidos"
    assert calculo("2 +") == "Expresion incompleta"
    assert calculo("2 + 3 + 4") == "Expresion invalida, demasiados operadores"