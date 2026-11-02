import pytest
from pathlib import Path

@pytest.fixture
def test_sample():
    path = Path(r"E:\learning-log\Testing_Pytest\src\testing_pytest\sample.txt")
    with open(path, "w+") as file:
        yield file

def test_add_sample(test_sample):
    test_sample.write("This is added through yield.py") 
    test_sample.seek(0)
    assert test_sample.read() == "This is added through yield.py"

