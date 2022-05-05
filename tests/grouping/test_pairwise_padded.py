from les_iterables.grouping import pairwise_padded


def test_pairwise_padded_empty():
    items = []
    actual = list(pairwise_padded(items))
    assert actual == []


def test_pairwise_padded_single():
    items = [5]
    actual = list(pairwise_padded(items))
    assert actual == [(5, None)]


def test_pairwise_padded_double():
    items = [5, 6]
    actual = list(pairwise_padded(items))
    assert actual == [(5, 6), (6, None)]


def test_pairwise_padded_triple():
    items = [5, 6, 7]
    actual = list(pairwise_padded(items))
    assert actual == [(5, 6), (6, 7), (7, None)]


def test_pairwise_padded_triple_fill_value():
    items = [5, 6, 7]
    actual = list(pairwise_padded(items, fillvalue=23))
    assert actual == [(5, 6), (6, 7), (7, 23)]
