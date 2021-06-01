from itertools import count

from pytest import raises

from les_iterables.combining import join_with


def test_join_with_empty_items_empty_separators():
    actual = list(join_with([], []))
    assert actual == []


def test_join_with_empty_items_redundant_separators_not_consumed():
    separators = count()
    list(join_with([], separators))
    assert next(separators) == 0


def test_join_with_items_and_separators_correct_lengths():
    actual = list(join_with(["A", "B", "C"], ["1", "2"]))
    assert actual == ["A", "1", "B", "2", "C"]


def test_too_few_separators_raises_value_error():
    with raises(ValueError):
        list(join_with(["A", "B", "C"], ["1"]))
