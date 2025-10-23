
from calculadora import suma,multiplicacion

def test_suma():
    assert suma(2,5) == 7

def test_multiplicacion():
    assert multiplicacion(3,5) == 15
