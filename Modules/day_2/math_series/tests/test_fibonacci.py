import pytest
from Modules.day_2.math_series.math_series.fibonacci_module import fibonacci


@pytest.mark.parametrize(
    "test_input, expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)]
)
def test_fibonacci(test_input, expected):
    assert fibonacci(test_input) == expected
