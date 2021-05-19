from pytest import raises

from les_iterables.selecting import previous


def test_previous_for_empty_collection_raises_value_error():
    with raises(ValueError):
        previous([], 5)


def test_previous_with_item_in_first_place_raises_value_error():
    with raises(ValueError):
        previous([5], 5)


def test_previous_with_item_missing_raises_value_error():
    with raises(ValueError):
        previous([3], 5)


def test_previous_with_item_present_returns_previous_item_1():
    assert previous([1, 2, 3], 2) == 1


def test_previous_with_item_present_returns_previous_item_2():
    assert previous([4, 5, 6], 6) == 5