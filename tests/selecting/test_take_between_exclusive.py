from les_iterables import take_between_exclusive


def test_take_between_exclusive_empty():
    assert list(take_between_exclusive([], lambda item: True, lambda item: True)) == []


def test_take_between_exclusive_no_start():
    assert list(take_between_exclusive([1, 2, 3], lambda item: item == 0, lambda item: True)) == []


def test_take_between_exclusive_no_end():
    assert list(take_between_exclusive([1, 2, 3], lambda item: True, lambda item: item == 4)) == []


def test_take_between_exclusive_no_start_or_end():
    assert list(take_between_exclusive([1, 2, 3], lambda item: item == 0, lambda item: item == 4)) == []


def test_take_between_exclusive_with_start_and_end():
    assert list(take_between_exclusive([1, 2, 3, 4, 5, 6], lambda item: item == 2, lambda item: item == 5)) == [3, 4]




