from les_iterables.selecting import take_between_inclusive, take_between_inclusive_values


def test_take_until_contains():
    items = [1, 6, 2, 9, 56]
    result = take_between_inclusive_values(items, 6, 9)
    assert result == [6, 2, 9]


def test_take_until_not_contains_first():
    items = [1, 6, 2, 9, 56]
    result = take_between_inclusive_values(items, 17, 9)
    assert result == []


def test_take_until_not_contains_last():
    items = [1, 6, 2, 9, 56]
    result = take_between_inclusive_values(items, 6, 17)
    assert result == []
