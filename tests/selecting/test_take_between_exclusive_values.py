from les_iterables.selecting import take_between_exclusive_values


def test_take_between_exclusive_values_empty():
    assert list(take_between_exclusive_values([], 1, 2)) == []


def test_take_between_exclusive_values_no_start():
    assert list(take_between_exclusive_values([1, 2, 3], 0, 2)) == []


def test_take_between_exclusive_values_no_end():
    assert list(take_between_exclusive_values([1, 2, 3], 1, 4)) == []


def test_take_between_exclusive_values_no_start_or_end():
    assert list(take_between_exclusive_values([1, 2, 3], 0, 4)) == []


def test_take_between_exclusive_values_with_start_and_end():
    assert list(take_between_exclusive_values([1, 2, 3, 4, 5, 6], 2, 5)) == [3, 4]
