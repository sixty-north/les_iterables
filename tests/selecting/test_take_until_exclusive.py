from les_iterables.selecting import take_until_exclusive


def test_take_until_exclusive_contains():
    items = [1, 6, 2, 9, 56]
    result = list(take_until_exclusive(items, lambda item: item == 2))
    assert result == [1, 6]


def test_take_until_exclusive_not_contains():
    items = [1, 6, 2, 9, 56]
    result = list(take_until_exclusive(items, lambda item: item == 17))
    assert result == [1, 6, 2, 9, 56]