from _pytest.python_api import raises

from les_iterables.selecting import relative_to


def test_relative_to_missing_item_raises_value_error():
    with raises(ValueError):
        relative_to([4, 6, 9], 12, offset=1)


def test_relative_by_negative_zero():
    assert relative_to([4, 6, 9], 6, offset=0) == 6


def test_relative_by_negative_one():
    assert relative_to([4, 6, 9], 6, offset=-1) == 4


def test_relative_by_positive_one():
    assert relative_to([4, 6, 9], 6, offset=+1) == 9


def test_relative_by_negative_two():
    assert relative_to([2, 4, 6, 9, 7], 9, offset=-2) == 4


def test_relative_by_positive_two():
    assert relative_to([2, 4, 6, 9, 7], 4, offset=+2) == 9


def test_relative_by_negative_two_out_of_range_raises_value_error():
    with raises(ValueError):
        relative_to([2, 4, 6, 9, 7], 4, offset=-2)


def test_relative_by_positive_two_out_of_range_raises_value_error():
    with raises(ValueError):
        relative_to([2, 4, 6, 9, 7], 9, offset=+2)


def test_relative_by_positive_two_to_oneth_occurrence():
    assert relative_to([2, 4, 5, 4, 6, 8, 10], 4, offset=2, n=1) == 8


def test_relative_by_negative_three_to_oneth_occurrence():
    assert relative_to([2, 4, 5, 4, 6, 8, 10], 4, offset=-3, n=1) == 2


def test_relative_to_missing_item_return_default():
    assert relative_to([4, 6, 9], 12, offset=1, default=38) == 38


def test_relative_by_negative_zero_with_default():
    assert relative_to([4, 6, 9], 6, offset=0, default=9) == 6


def test_relative_by_negative_one_with_default():
    assert relative_to([4, 6, 9], 6, offset=-1, default=14) == 4


def test_relative_by_positive_one_with_default():
    assert relative_to([4, 6, 9], 6, offset=+1, default=5) == 9


def test_relative_by_negative_two_with_default():
    assert relative_to([2, 4, 6, 9, 7], 9, offset=-2, default=16) == 4


def test_relative_by_positive_two_with_default():
    assert relative_to([2, 4, 6, 9, 7], 4, offset=+2, default=12) == 9


def test_relative_by_negative_two_out_of_range_raises_value_error_with_default():
    assert relative_to([2, 4, 6, 9, 7], 4, offset=-2, default=97) == 97


def test_relative_by_positive_two_out_of_range_raises_value_error_with_default():
    assert relative_to([2, 4, 6, 9, 7], 9, offset=+2, default=67) == 67


def test_relative_by_positive_two_to_oneth_occurrence_with_default():
    assert relative_to([2, 4, 5, 4, 6, 8, 10], 4, offset=2, n=1, default=12) == 8


def test_relative_by_negative_three_to_oneth_occurrence_with_default():
    assert relative_to([2, 4, 5, 4, 6, 8, 10], 4, offset=-3, n=1, default=37) == 2
