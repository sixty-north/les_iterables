from pytest import raises

from les_iterables.selecting import element_at


def test_element_at_empty():
    with raises(IndexError):
        element_at([], 0)


def test_element_at_single():
    assert element_at([1], 0) == 1


def test_element_at_single_out_of_bounds_start():
    with raises(IndexError):
        element_at([], -1)


def test_element_at_single_out_of_bounds_end():
    with raises(IndexError):
        element_at([1], 1)


def test_element_at_multiple():
    assert element_at([1, 2, 3], 1) == 2


def test_element_at_start_at_one():
    assert element_at([1, 2, 3], 1, start=1) == 1