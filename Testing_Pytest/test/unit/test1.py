from testing_pytest.main import add, divide
import pytest 

def test_add():
    assert add(5, 2) == 7
    assert add(0, 2) == 2
    assert add(5, -76) == -71

def test_divide():
    assert divide(6,2) == 3

    with pytest.raises(ValueError, match="Can't divide by zero"):
        divide(5,0)