from les_iterables.selecting import take_after_exclusive


def test_take_after_exclusive_empty():
    assert list(take_after_exclusive([], lambda item: True)) == []


def test_take_after_exclusive_no_match():
    assert list(take_after_exclusive([1, 2, 3], lambda item: item == 4)) == []


def test_take_after_exclusive_match():
    assert list(take_after_exclusive([1, 2, 3, 4, 5], lambda item: item == 3)) == [4, 5]


