from les_iterables.grouping import split_after_first


def test_split_after_first_empty_returns_one_empty_group():
    actual = list(split_after_first([], lambda x: x))
    assert actual == [[]]


def test_split_after_first_non_matching_predicate_returns_one_group():
    actual = list(split_after_first([1, 2, 3], lambda x: False))
    assert actual == [[1, 2, 3]]


def test_split_string_after_first_non_matching_predicate_returns_one_group():
    actual = list(split_after_first('abcd', lambda x: x == 'n'))
    assert actual == ['abcd']


def test_split_after_first_matching_predicate_in_the_beginning_returns_two_groups():
    actual = list(split_after_first([1, 2, 3], lambda x: x == 1))
    assert actual == [[1], [2, 3]]


def test_split_tuple_after_first_matching_predicate_in_the_beginning_returns_two_groups():
    actual = list(split_after_first((1, 2, 3), lambda x: x == 1))
    assert actual == [(1,), (2, 3)]


def test_split_after_first_matching_predicate_in_the_middle_returns_two_groups():
    actual = list(split_after_first([1, 2, 3], lambda x: x == 2))
    assert actual == [[1, 2], [3]]


def test_split_string_after_first_matching_predicate_in_the_middle_returns_two_groups():
    actual = list(split_after_first('abcde', lambda x: x == 'c'))
    assert actual == ['abc', 'de']


def test_split_after_first_matching_predicate_at_the_end_returns_one_group():
    actual = list(split_after_first([1, 2, 3], lambda x: x == 3))
    assert actual == [[1, 2, 3]]


def test_split_after_first_only_splits_on_first_match():
    actual = list(split_after_first([1, 2, 3, 1, 2, 3], lambda x: x == 2))
    assert actual == [[1, 2], [3, 1, 2, 3]]


def test_split_after_first_producing_two_groups_can_be_unpacked():
    group, *groups = split_after_first([1, 2, 3, 1, 2, 3], lambda x: x == 2)
    assert group == [1, 2]
    assert groups == [[3, 1, 2, 3]]


def test_split_after_first_producing_one_group_can_be_unpacked():
    group, *groups = split_after_first([1, 2, 3], lambda x: x == 3)
    assert group == [1, 2, 3]
    assert groups == []
