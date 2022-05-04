from pytest import raises

from les_iterables import partition_tail


def test_partition_tail_empty():
    head, tail = partition_tail([], 1)
    assert list(head) == []
    assert list(tail) == []


def test_partition_tail_zero():
    head, tail = partition_tail([2, 4, 6, 8], 0)
    assert list(head) == [2, 4, 6, 8]
    assert list(tail) == []


def test_partition_tail_one():
    head, tail = partition_tail([2, 4, 6, 8], 1)
    assert list(head) == [2, 4, 6]
    assert list(tail) == [8]


def test_partition_tail_two():
    head, tail = partition_tail([2, 4, 6, 8], 2)
    assert list(head) == [2, 4]
    assert list(tail) == [6, 8]


def test_partition_tail_all():
    head, tail = partition_tail([2, 4, 6, 8], 4)
    assert list(head) == []
    assert list(tail) == [2, 4, 6, 8]


def test_partition_tail_more():
    head, tail = partition_tail([2, 4, 6, 8], 5)
    assert list(head) == []
    assert list(tail) == [2, 4, 6, 8]


def test_partition_tail_negative_raises_value_error():
    with raises(ValueError):
        partition_tail([2, 4, 6, 8], -1)