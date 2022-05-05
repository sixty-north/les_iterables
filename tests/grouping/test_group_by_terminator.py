from les_iterables.grouping import group_by_terminator


def test_group_by_terminator_empty():
    items = []
    actual = list(group_by_terminator(items, lambda x: x == 10))
    assert actual == []


def test_group_by_terminator_single_non_matching():
    items = [3]
    actual = list(group_by_terminator(items, lambda x: x == 10))
    assert actual == [[3]]


def test_group_by_terminator_single_matching():
    items = [10]
    actual = list(group_by_terminator(items, lambda x: x == 10))
    assert actual == [[10]]


def test_group_by_terminator_double_matching():
    items = [10, 10]
    actual = list(group_by_terminator(items, lambda x: x == 10))
    assert actual == [[10], [10]]


def test_group_by_terminator_double_non_matching():
    items = [3, 8]
    actual = list(group_by_terminator(items, lambda x: x == 10))
    assert actual == [[3, 8]]


def test_group_by_terminator_single_terminated_group():
    items = [3, 8, 10]
    actual = list(group_by_terminator(items, lambda x: x == 10))
    assert actual == [[3, 8, 10]]


def test_group_by_terminator_two_terminated_groups():
    items = [3, 8, 10, 5, 6, 10]
    actual = list(group_by_terminator(items, lambda x: x == 10))
    assert actual == [[3, 8, 10], [5, 6, 10]]


def test_group_by_terminator_one_terminated_group_and_one_unterminated_group():
    items = [3, 8, 10, 5, 6]
    actual = list(group_by_terminator(items, lambda x: x == 10))
    assert actual == [[3, 8, 10], [5, 6]]

