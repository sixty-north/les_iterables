from les_iterables.selecting import transform_if


def test_transform_if_empty():
    items = []
    actual = list(transform_if(items, lambda x: x % 2 != 0, lambda x: x*x))
    assert actual == []


def test_transform_if_empty_single_non_matching():
    items = [4]
    actual = list(transform_if(items, lambda x: x % 2 != 0, lambda x: x*x))
    assert actual == [4]


def test_transform_if_empty_single_matching():
    items = [3]
    actual = list(transform_if(items, lambda x: x % 2 != 0, lambda x: x*x))
    assert actual == [9]


def test_transform_if_series():
    items = [1, 2, 3, 4, 5, 6]
    actual = list(transform_if(items, lambda x: x % 2 != 0, lambda x: x*x))
    assert actual == [1, 2, 9, 4, 25, 6]
