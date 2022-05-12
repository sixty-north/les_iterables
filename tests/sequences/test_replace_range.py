from pytest import raises

from les_iterables.sequences import replace_range


def test_replace_empty_range_empty_with_empty():
    assert replace_range([], range(0, 0), []) == []


def test_replace_empty_range_at_beginning_with_empty_sequence():
    assert replace_range([1, 2, 3], range(0, 0), []) == [1, 2, 3]


def test_replacing_empty_range_at_beginning_with_non_empty_sequence_inserts():
    assert replace_range([1, 2, 3], range(0, 0), [-1, 0]) == [-1, 0, 1, 2, 3]


def test_replace_non_empty_range_at_beginning_with_empty_sequence_removes():
    assert replace_range([1, 2, 3], range(0, 2), []) == [3]


def test_replace_non_empty_range_at_beginning_with_non_empty_sequence_replaces():
    assert replace_range([1, 2, 3], range(0, 2), [8, 9, 10]) == [8, 9, 10, 3]


def test_replace_non_empty_range_in_middle_with_non_empty_sequence_replaces():
    assert replace_range([1, 2, 3], range(1, 2), [8, 9, 10]) == [1, 8, 9, 10, 3]


def test_replace_with_inverted_range_duplicates_items():
    assert replace_range([1, 2, 3], range(2, 1), [8, 9, 10]) == [1, 2, 8, 9, 10, 2, 3]


def test_replace_range_with_string():
    assert replace_range("oldfoundland", range(0, 3), "new") == "newfoundland"


def test_replace_range_with_string_using_slice():
    assert replace_range("oldfoundland", slice(0, 3), "new") == "newfoundland"


def test_replace_range_with_string_using_slice_with_non_unity_step_raises_value_error():
    with raises(ValueError):
        replace_range("oldfoundland", slice(0, 3, 2), "new")