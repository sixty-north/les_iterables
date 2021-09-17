from operator import itemgetter

from les_iterables.searching import duplicates


def test_empty():
    t = []
    d = list(duplicates(t))
    assert d == []


def test_no_duplicates():
    t = [5, 3, 2, 7, 9]
    d = list(duplicates(t))
    assert d == []


def test_one_single_duplicate():
    t = [1, 3, 3, 9]
    d = list(duplicates(t))
    assert d == [3]


def test_two_single_duplicates():
    t = [1, 3, 6, 3, 6, 2, 9]
    d = list(duplicates(t))
    assert d == [3, 6]


def test_duplicates_is_lazy():
    def source_values():
        yield 67
        yield 34
        yield 34
        assert False, "Do not iterate this far!"
    assert next(duplicates(source_values())) == 34


def test_one_single_one_double_duplicate():
    t = [1, 3, 6, 3, 6, 2, 9, 3]
    d = list(duplicates(t))
    assert d == [3, 6, 3]


def test_with_key():
    t = "AbCDeFfGGhhHijkKk"
    d = ''.join(duplicates(t, key=str.lower))
    assert d == "fGhHKk"


def test_with_non_hashable_elements():
    t = ([1, 2], [2, 3], [1, 2])
    d = list(duplicates(t))
    assert d == [[1, 2]]


def test_with_mixed_hashable_and_non_hashable_elements():
    t = (1, 3, 7, 9, 7, [1, 2], [2, 3], [1, 2])
    d = list(duplicates(t))
    assert d == [7, [1, 2]]


def test_with_mixed_hashable_and_multiple_non_hashable_elements():
    t = (1, 3, 7, 9, 7, [1, 2], [2, 3], [1, 2], [2, 3], [5, 6])
    d = list(duplicates(t))
    assert d == [7, [1, 2], [2, 3]]


def test_with_hashable_key_of_non_hashable_elements():
    t = ([1, 2], [2, 3], [1, 2], [2, 3], [5, 6])
    d = list(duplicates(t, key=tuple))
    assert d == [[1, 2], [2, 3]]


def test_with_dictionary_items():
    t = [
        {"name": "John", "age": 23},
        {"name": "Bill", "age": 47},
        {"name": "Iris", "age": 19},
        {"name": "Rose", "age": 98},
        {"name": "Rose", "age": 35},
    ]
    d = list(duplicates(t, key=itemgetter("name")))
    assert d == [
        {"name": "Rose", "age": 35},
    ]
