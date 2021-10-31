from les_iterables.selecting import skip_while


def test_skip_while_empty():
    actual = list(skip_while([], lambda x: x%2 == 0))
    assert actual == []


def test_skip_while_leaving_empty():
    actual = list(skip_while([4], lambda x: x%2 == 0))
    assert actual == []


def test_skip_while_none_to_skip_yielding_one():
    actual = list(skip_while([3], lambda x: x%2 == 0))
    assert actual == [3]


def test_skip_while_one_to_skip_yielding_one():
    actual = list(skip_while([2, 5], lambda x: x%2 == 0))
    assert actual == [5]


def test_skip_while_none_to_skip_yielding_two():
    actual = list(skip_while([3, 7], lambda x: x%2 == 0))
    assert actual == [3, 7]


def test_skip_while_one_to_skip_yielding_two():
    actual = list(skip_while([2, 5, 9], lambda x: x%2 == 0))
    assert actual == [5, 9]


def test_skip_while_two_to_skip_yielding_two():
    actual = list(skip_while([2, 4, 5, 9], lambda x: x%2 == 0))
    assert actual == [5, 9]

def test_skip_while_later_matches_yielded():
    actual = list(skip_while([2, 4, 5, 9, 6], lambda x: x%2 == 0))
    assert actual == [5, 9, 6]