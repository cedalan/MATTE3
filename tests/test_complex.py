import pytest
from complex_lib.complex import Complex

@pytest.fixture
def z1():
    return Complex(2, 3)

@pytest.fixture
def z2():
    return Complex(1, 4)

def test_addition(z1, z2):
    result = z1 + z2

    assert result.real == 3
    assert result.imag == 7

def test_subtraction(z1, z2):
    result = z1 - z2

    assert result.real == 1
    assert result.imag == -1

def test_multiplication(z1, z2):
    result = z1 * z2

    assert result.real == -10
    assert result.imag == 11

def test_scalar_multiplication(z1):
    result = 2 * z1

    assert result.real == 4
    assert result.imag == 6

    result = 2.0 * z1

    assert result.real == 4
    assert result.imag == 6
