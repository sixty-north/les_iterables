from collections import deque

from pytest import raises

from les_iterables.sequences import pop_n


def test_pop_n_empty():
    seq = []

    with raises(IndexError):
        pop_n(seq, 1)


def test_pop_n_one():
    seq = [42]
    popped = pop_n(seq, 1)
    assert seq == []
    assert popped == [42]


def test_pop_n_too_many():
    seq = [42]
    with raises(IndexError):
        pop_n(seq, 2)


def test_pop_n_all():
    seq = [45, 67, 89, 12]
    popped = pop_n(seq, 4)
    assert seq == []
    assert popped == [45, 67, 89, 12]


def test_pop_n_partial():
    seq = [45, 67, 89, 12]
    popped = pop_n(seq, 2)
    assert seq == [45, 67]
    assert popped == [89, 12]


def test_pop_n_preserves_type():
    seq = deque([45, 67, 89, 12])
    popped = pop_n(seq, 2)
    assert seq == deque([45, 67])
    assert popped == deque([89, 12])


def test_pop_n_factory():
    seq = deque([45, 67, 89, 12])
    popped = pop_n(seq, 2, tuple)
    assert seq == deque([45, 67])
    assert popped == (89, 12)
