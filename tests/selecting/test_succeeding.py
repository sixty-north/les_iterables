from pytest import raises

from les_iterables.selecting import succeeding


def test_succeeding_for_empty_collection_raises_value_error():
    with raises(ValueError):
        succeeding([], 5)


def test_succeeding_with_item_in_last_place_raises_value_error():
    with raises(ValueError):
        succeeding([5], 5)


def test_succeeding_with_item_missing_raises_value_error():
    with raises(ValueError):
        succeeding([3], 5)


def test_succeeding_with_item_present_returns_succeeding_item_1():
    assert succeeding([1, 2, 3], 2) == 3


def test_succeeding_with_item_present_returns_succeeding_item_2():
    assert succeeding([4, 5, 6], 4) == 5