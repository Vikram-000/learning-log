import pytest
from testing_pytest.grade_calculator import GradeCalculator

@pytest.fixture
def calculator():
    return GradeCalculator()

@pytest.mark.parametrize(
    "marks, expected" ,
    [
        (95, "A"),
        (85, "B"),
        (65, "C"),
        (45, "D"),
        (30, "F"),
        (0, "F"),
        (100, "A")
    ]
)

def test_calculate_grade(calculator, marks, expected):
    assert calculator.calculate_grade(marks) == expected

@pytest.mark.parametrize(
    "marks",
    [
        (-10),
        (101),
        (121)
    ]
)

def test_calculate_garde_invalid(calculator, marks):
    with pytest.raises(ValueError, match="Marks must be between 0 and 100"):
        calculator.calculate_grade(marks)