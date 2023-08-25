import sys

from hypothesis import given
from hypothesis.strategies import lists, integers

from les_iterables import complete_chunks


def test_complete_chunks_empty():
    assert list(complete_chunks([], 3)) == []


def test_complete_chunks_less_than_n():
    assert list(complete_chunks([1, 2], 3)) == []


def test_complete_chunks_equal_to_n():
    assert list(complete_chunks([1, 2, 3], 3)) == [[1, 2, 3]]


def test_complete_chunks_greater_than_n():
    assert list(complete_chunks([1, 2, 3, 4], 3)) == [[1, 2, 3]]


def test_complete_chunks_equal_to_2n():
    assert list(complete_chunks([1, 2, 3, 4, 5, 6], 3)) == [[1, 2, 3], [4, 5, 6]]


def test_complete_chunks_greater_than_2n():
    assert list(complete_chunks([1, 2, 3, 4, 5, 6, 7], 3)) == [[1, 2, 3], [4, 5, 6]]


@given(
    items=lists(integers()),
    size=integers(min_value=1, max_value=sys.maxsize)
)
def test_complete_chunks_all_have_expected_chunk_size(items, size):
    assert all(len(chunk) == size for chunk in complete_chunks(items, size))


def test_complete_chunks_with_empty_string():
    assert list(complete_chunks("", 3)) == []


def test_complete_chunks_with_string_less_than_n():
    assert list(complete_chunks("ab", 3)) == []


def test_complete_chunks_with_string_equal_to_n():
    assert list(complete_chunks("abc", 3)) == ["abc"]


def test_complete_chunks_with_string_greater_than_n():
    assert list(complete_chunks("abcd", 3)) == ["abc"]


def test_complete_chunks_with_string_equal_to_2n():
    assert list(complete_chunks("abcdef", 3)) == ["abc", "def"]


def test_complete_chunks_with_string_greater_than_2n():
    assert list(complete_chunks("abcdefg", 3)) == ["abc", "def"]


def test_complete_chunks_with_empty_tuple():
    assert list(complete_chunks((), 3)) == []


def test_complete_chunks_with_tuple_less_than_n():
    assert list(complete_chunks((1, 2), 3)) == []


def test_complete_chunks_with_tuple_equal_to_n():
    assert list(complete_chunks((1, 2, 3), 3)) == [(1, 2, 3)]


def test_complete_chunks_with_tuple_greater_than_n():
    assert list(complete_chunks((1, 2, 3, 4), 3)) == [(1, 2, 3)]


def test_complete_chunks_with_tuple_equal_to_2n():
    assert list(complete_chunks((1, 2, 3, 4, 5, 6), 3)) == [(1, 2, 3), (4, 5, 6)]


def test_complete_chunks_with_tuple_greater_than_2n():
    assert list(complete_chunks((1, 2, 3, 4, 5, 6, 7), 3)) == [(1, 2, 3), (4, 5, 6)]


def test_complete_chunks_with_empty_and_explicit_group_factory():
    assert list(complete_chunks([], 3, group_factory=set)) == []


def test_complete_chunks_with_less_than_n_and_explicit_group_factory():
    assert list(complete_chunks([1, 2], 3, group_factory=set)) == []


def test_complete_chunks_with_equal_to_n_and_explicit_group_factory():
    assert list(complete_chunks([1, 2, 3], 3, group_factory=set)) == [{1, 2, 3}]


def test_complete_chunks_with_greater_than_n_and_explicit_group_factory():
    assert list(complete_chunks([1, 2, 3, 4], 3, group_factory=set)) == [{1, 2, 3}]


def test_complete_chunks_with_equal_to_2n_and_explicit_group_factory():
    assert list(complete_chunks([1, 2, 3, 4, 5, 6], 3, group_factory=set)) == [{1, 2, 3}, {4, 5, 6}]


def test_complete_chunks_with_greater_than_2n_and_explicit_group_factory():
    assert list(complete_chunks([1, 2, 3, 4, 5, 6, 7], 3, group_factory=set)) == [{1, 2, 3}, {4, 5, 6}]