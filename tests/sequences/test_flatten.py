from les_iterables import concat
from les_iterables.combining import flatten


def test_flatten_empty():
    assert list(flatten([])) == []


def test_flatten_single_item():
    assert list(flatten([1])) == [1]


def test_flatten_string():
    assert list(flatten("abc")) == ['a', 'b', 'c']


def test_dont_flatten_string():
    assert list(flatten("abc", lambda x: isinstance(x, str))) == ['abc']


def test_flatten_list_of_strings():
    assert list(flatten(["abc", "def"])) == ['a', 'b', 'c', 'd', 'e', 'f']


def test_don_flatten_list_of_strings():
    assert list(flatten(["abc", "def"], lambda x: isinstance(x, str))) == ["abc", "def"]


def test_flatten_list_of_lists():
    assert list(flatten([[1, 2], [3, 4]])) == [1, 2, 3, 4]


def test_flatten_list_of_lists_of_strings():
    assert list(flatten([["abc", "def"], ["ghi", "jkl"]])) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']


def test_flatten_list_of_lists_of_strings_without_string_flattening():
    assert list(flatten([["abc", "def"], ["ghi", "jkl"]], lambda x: isinstance(x, str))) == ["abc", "def", "ghi", "jkl"]