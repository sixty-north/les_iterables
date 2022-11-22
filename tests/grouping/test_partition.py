from les_iterables.grouping import partition


def test_partition_around_matching_separator_returns_three_groups():
    before, separator, after = partition([1, 2, 3, 4], lambda x: x == 2)
    assert before == [1]
    assert separator == [2]
    assert after == [3, 4]


def test_partition_around_one_of_matching_separators_returns_three_groups():
    before, separator, after = partition('abcdede', lambda x: x == 'd')
    assert before == 'abc'
    assert separator == 'd'
    assert after == 'ede'


def test_partition_around_non_matching_separator_returns_three_groups():
    before, separator, after = partition((8, 16, 32), lambda x: x > 128)
    assert before == (8, 16, 32)
    assert separator == ()
    assert after == ()


def test_partition_around_first_element_in_iterator_returns_three_groups():
    input = [1, 2, 3, 4, 5]
    iterator = iter(input)
    before, separator, after = partition(iterator, lambda x: x == 1)
    assert before == []
    assert separator == [1]
    assert after == [2, 3, 4, 5]

