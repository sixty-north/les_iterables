from pytest import raises

from les_iterables.selecting import offset_iterators


def test_offset_iterators_on_empty_iterable_with_zero_offset():
    s = []
    p, q = offset_iterators(s, 0)
    with raises(StopIteration):
        next(p)
    with raises(StopIteration):
        next(q)


def test_zero_offset_iterators_on_non_empty_collection_yield_identical_items():
    s = [6, 9, 3, 2, 1]
    iter_p, iter_q = offset_iterators(s, 0)
    assert all(p == q for p, q in zip(iter_p, iter_q))


def test_leading_by_one_iterator_on_non_empty_collection():
    s = [6, 9, 3, 2, 1]
    iter_p, iter_q = offset_iterators(s, 1)
    ps = list(iter_p)
    qs = list(iter_q)
    assert ps == [6, 9, 3, 2, 1]
    assert qs == [9, 3, 2, 1]


def test_trailing_by_one_iterator_on_non_empty_collection():
    s = [6, 9, 3, 2, 1]
    iter_p, iter_q = offset_iterators(s, -1)
    ps = list(iter_p)
    qs = list(iter_q)
    assert ps == [9, 3, 2, 1]
    assert qs == [6, 9, 3, 2, 1]


def test_leading_by_two_iterator_on_non_empty_collection():
    s = [6, 9, 3, 2, 1]
    iter_p, iter_q = offset_iterators(s, 2)
    ps = list(iter_p)
    qs = list(iter_q)
    assert ps == [6, 9, 3, 2, 1]
    assert qs == [3, 2, 1]


def test_trailing_by_two_iterator_on_non_empty_collection():
    s = [6, 9, 3, 2, 1]
    iter_p, iter_q = offset_iterators(s, -2)
    ps = list(iter_p)
    qs = list(iter_q)
    assert ps == [3, 2, 1]
    assert qs == [6, 9, 3, 2, 1]



def test_leading_by_two_iterator_on_collection_of_two_gives_empty_iterator():
    s = [6, 9]
    iter_p, iter_q = offset_iterators(s, 2)
    ps = list(iter_p)
    qs = list(iter_q)
    assert ps == [6, 9]
    assert qs == []


def test_trailing_by_two_iterator_on_collection_of_two_gives_empty_iterator():
    s = [6, 9]
    iter_p, iter_q = offset_iterators(s, -2)
    ps = list(iter_p)
    qs = list(iter_q)
    assert ps == []
    assert qs == [6, 9]



def test_leading_by_three_iterator_on_too_short_collection_raises_value_error():
    s = [6, 9]
    with raises(ValueError):
        offset_iterators(s, 3)


def test_trailing_by_three_iterator_on_too_short_collection_raises_value_error():
    s = [6, 9]
    with raises(ValueError):
        offset_iterators(s, -3)
