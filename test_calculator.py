from calculator import add, substract, multiply, create, create


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1


def test_substract():
    assert substract(5, 1) == 4
    assert substract(1, 5) == -4


def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(5, -2) == -10
