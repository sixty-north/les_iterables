from les_iterables.selecting import take_after_inclusive, take_before_inclusive


def test_take_before_inclusive_contains():
    items = [1, 6, 2, 9, 56]
    result = list(take_before_inclusive(items, lambda item: item == 2))
    assert result == [1, 6, 2]


def test_take_before_inclusive_not_contains():
    items = [1, 6, 2, 9, 56]
    result = list(take_before_inclusive(items, lambda item: item == 17))
    assert result == []

