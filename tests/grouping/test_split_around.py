from les_iterables.grouping import split_around


def test_split_around_empty_returns_no_groups():
    actual = list(split_around([], lambda x: x))
    assert actual == []


def test_split_around_one_matching_returns_one_group():
    items = [5]
    actual = list(split_around(items, lambda x: x == 5))
    assert actual == [[5]]


def test_split_around_one_not_matching_returns_one_group():
    items = [7]
    actual = list(split_around(items, lambda x: x == 5))
    assert actual == [[7]]


def test_split_around_two_with_only_first_matching_returns_two_groups():
    items = [5, 7]
    actual = list(split_around(items, lambda x: x == 5))
    assert actual == [[5], [7]]


def test_split_around_two_with_only_second_matching_returns_two_groups():
    items = [7, 5]
    actual = list(split_around(items, lambda x: x == 5))
    assert actual == [[7], [5]]


def test_split_around_three_with_only_middle_matching_returns_three_groups():
    items = [7, 5, 4]
    actual = list(split_around(items, lambda x: x == 5))
    assert actual == [[7], [5], [4]]


def test_split_around_runs_of_non_matching_items_in_groups():
    items = [7, 3, 5, 2, 4]
    actual = list(split_around(items, lambda x: x == 5))
    assert actual == [[7, 3], [5], [2, 4]]


def test_split_around_consecutive_matching_items_in_separate_groups():
    items = [7, 3, 5, 5, 2, 4]
    actual = list(split_around(items, lambda x: x == 5))
    assert actual == [[7, 3], [5], [5], [2, 4]]


def test_split_around_group_factory():
    items = [7, 3, 5, 5, 2, 4]
    actual = list(split_around(items, lambda x: x == 5, group_factory=tuple))
    assert actual == [(7, 3), (5,), (5,), (2, 4)]