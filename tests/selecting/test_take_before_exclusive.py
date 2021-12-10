from les_iterables.selecting import take_before_exclusive


def test_take_before_inclusive_contains():
    items = [1, 6, 2, 9, 56]
    result = list(take_before_exclusive(items, lambda item: item == 2))
    assert result == [1, 6]


def test_take_before_inclusive_not_contains():
    items = [1, 6, 2, 9, 56]
    result = list(take_before_exclusive(items, lambda item: item == 17))
    assert result == []
