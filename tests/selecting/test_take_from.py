from les_iterables.selecting import take_after_inclusive


def test_take_after_inclusive_contains():
    items = [1, 6, 2, 9, 56]
    result = list(take_after_inclusive(items, lambda item: item == 2))
    assert result == [2, 9, 56]


def test_take_after_inclusive_not_contains():
    items = [1, 6, 2, 9, 56]
    result = list(take_after_inclusive(items, lambda item: item == 17))
    assert result == []
