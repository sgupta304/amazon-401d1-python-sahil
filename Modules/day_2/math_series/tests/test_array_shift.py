import pytest

from Modules.day_2.math_series.math_series.array_shift import insert_shift_array


@pytest.mark.parametrize(
    "test_input_arr, val_to_insert, expected", [([1, 2, 3], 3, [1, 2, 3, 3])]
)
def test_arr_shift(test_input_arr, val_to_insert, expected):
    assert insert_shift_array(test_input_arr, val_to_insert) == expected
